from celery import shared_task
from rest_framework.response import Response
from rest_framework import status
from JobExecuter.models import ExecutedJob, Status
from Main_API.models import Job
from subprocess import run
import time, os


INPUT_FOLDER_PATH = 'JobExecuter/jobs/'
OUTPUT_FOLDER_PATH = 'JobExecuter/jobs/'

def create_input_file (filename, data):
    written = 0
    cwd = os.getcwd()
    print (cwd)
    ifile = open(filename, 'a')
    written = ifile.write(data)
    ifile.close()
    return written

def delete_input_file (filename):
    if os.path.exists(filename):
        os.remove(filename)
        return True
    else:
        return False


@shared_task
def execute (request_data, job_data):
    #print (request_data)
    user_id = request_data['user_id']
    job_id = request_data['job_id']
    filename = request_data['filename']
    data = request_data['data']
    arguments = request_data['arguments']

    job = Job.objects.get(id=job_id)
    executed_job = ExecutedJob.objects.get(id=job_data.id)
    path = job.path
    jobname = job.name
    file_extension = job.output_type.all()[0]

    # CREATE OUTPUT NAME BASED ON THE USER ID, JOB ID AND CURRENT TIME
    exec_time = job_data.execution_time.strftime("%Y%m%d%H%M%S")
    input_name = INPUT_FOLDER_PATH + exec_time + filename
    #input_name = filename
    output_name = str(user_id) + str(job_id) + str(exec_time) + str(file_extension)
    
    # WRITE DATA TO A TEMP FILE FOR PROCESSING
    create_input_file (input_name, data)

    input = input_name
    output = "{}{}".format(OUTPUT_FOLDER_PATH, output_name)

    # CREATE ARGUMENT LIST FOR COMMAND
    argv = [path, input, output] + arguments
    
    # UPDATE STATUS TO "RUNNING"
    executed_job.status = Status.objects.get(id=2)
    executed_job.save(update_fields=['status'])
    
    #print (argv)
    start = time.time()
    process = run (argv)
    end = time.time()
    exec_time = end - start

    # DELETE INPUT FILE
    deleted = delete_input_file (input_name)
    #print (deleted)
    if process.returncode == 0:
        # UPDATE  STATUS TO "FINISHED"
        executed_job.status = Status.objects.get(id=4)
        executed_job.running_time = exec_time
        executed_job.output = output
        executed_job.save(update_fields=['status', 'running_time', 'output'])

        success_message = "Proceso {} ejecutado correctamente en {}s. Puedes encontrar el resultado en tus procesos ejecutados.".format(jobname, exec_time)
        success_data = {
            "success_message": success_message,
            "return_value": process.returncode,
            "output_url": output,
            "executed_job_id": job_data.id
        }
        return Response(status=status.HTTP_200_OK, data=success_data)
        
    else:
        # UPDATE STATUS TO "TERMINATED"
        executed_job.status = Status.objects.get(id=3)
        executed_job.save(update_fields=['status'])

        error_message = "Error al ejecutar el proceso {} con código de retorno {}".format(jobname, process.returncode)
        error_data = {
            "error_message": error_message,
            "return_value": process.returncode,
            "executed_job_id": job_data.id
        }
        return Response(status= status.HTTP_400_BAD_REQUEST, data=error_data)
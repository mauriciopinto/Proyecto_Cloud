import axios from 'axios'

let CONDATA_JOB_URL = "http://192.168.59.117:32647/job/"
let CONDATA_API_URL = "http://192.168.59.117:32647/api/"

export function getExecutedJobsByUser (userId) {
    let url = CONDATA_JOB_URL + 'run_jobs?user_id=' + userId

    return axios.get(url)
}

export function getJobDataById (jobId) {
    let url = CONDATA_API_URL + 'jobs?id=' + jobId

    return axios.get(url)
}

export function getArgumentsByJobId (jobId) {
    let url = CONDATA_API_URL + 'arguments?job_id=' + jobId

    return axios.get(url)
}

export function executeJob (jobData) {
    let url = CONDATA_JOB_URL + 'execute/'

    console.log (jobData)
    return axios.post(url, jobData)
}

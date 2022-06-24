import React from 'react'
import { PageHeader, SectionHeader } from '../Components/Header'
import { List } from '../Components/List'
import { getJobsByClientId, getSessionUserData } from '../Services/Account/User'
import { getExecutedJobsByUser } from '../Services/Account/Job'
import { RegularTable } from '../Components/Table'
import NavBar from '../Components/NavBar'

let CONDATA_SERVER_JOB_OUPUT = "http://localhost:8000/job/output"

let navBarElements = [
    {text: "Inicio", link: "/user"},
    {text: "Cerrar Sesión", link: "/logout"}
]

let executedJobsHeaders = [
    "Nombre",
    "Fecha y hora de inicio",
    "Estado",
    "Tiempo de ejecución",
    "Resultado"
]

let statusCodes = {
    1: "Creado",
    2: "En ejecución",
    3: "Error al ejecutar",
    4: "Completado"
}

class UserPage extends React.Component {
    constructor (props) {
        super (props)

        this.state = {userId: null, username: null, clientId: null, jobs: null, executedJobs: null, logged: null}
    }

    componentDidMount () {
        getSessionUserData ()
        .then (res => {
            this.setState({userId: res.data.id, username: res.data.username, clientId: res.data.client_id, logged: true},
                            () => {
                                getJobsByClientId(res.data.client_id)
                                .then ((res) => {
                                    let jobs = res.data.map ((job, i) => {
                                        return <li key={i}><a href={"/job/" + job.id}>{job.name}</a></li>
                                    })
                                    this.setState({jobs: jobs})
                                    getExecutedJobsByUser(this.state.userId)
                                    .then ((res) => {
                                        console.log (res)
                                        let executedJobs = res.data.map((xJob) => {
                                            let element = <tr><td>{xJob.tagname}</td><td>{Date(xJob.execution_time).toString()}</td><td>{statusCodes[xJob.status]}</td><td>{xJob.running_time}</td><td><a href={CONDATA_SERVER_JOB_OUPUT + "?file=" + xJob.output} download>Archivo de salida</a></td></tr>
                                            return element
                                        })
                                        this.setState({executedJobs: executedJobs})
                                    })
                                })
                            })

        })
        .then ((res) => res)
        .catch((err) => {
            alert(err.response.data.error_message)
            window.location.href = '/login'
        })
    }

    render () {
        console.log ("rendering", this.state)
        if (!this.state.logged) {
            return <></>
        }
        else {
            return (
                <div id="user-page">
                    <NavBar elements={navBarElements}/>
                    <PageHeader text={"Bienvenido, " + this.state.username} id="user-page-header"/>
                    <SectionHeader text="Tus procesos" id="user-page-joblist-header" />
                    <List elements={this.state.jobs} id="user-page-joblist" />
                    <br></br>
                    <SectionHeader text="Procesos ejecutados recientemente" id="user-page-executed-joblist-header" />
                    <RegularTable elements={this.state.executedJobs} id="user-page-executed-joblist" headers={executedJobsHeaders}/>
                </div>
            )
        }
    }
}

export default UserPage
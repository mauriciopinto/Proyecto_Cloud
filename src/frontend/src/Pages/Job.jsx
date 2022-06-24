import React from "react"
import { RegularForm } from "../Components/Form"
import { PageHeader } from "../Components/Header"
import { RegularLink } from "../Components/Link"
import { RegularText } from "../Components/Text"
import { getJobDataById, executeJob, getArgumentsByJobId } from "../Services/Account/Job"
import { getSessionUserData } from "../Services/Account/User"
import NavBar from '../Components/NavBar'

let navBarElements = [
    {text: "Inicio", link: "/user"},
    {text: "Cerrar Sesión", link: "/logout"}
]

class JobPage extends React.Component {
    constructor (props) {
        super (props)

        this.state = {jobId: null,
                      jobName: null, 
                      inputFile: null,
                      userId: null,
                      userName: null,
                      description: null,
                      argCount: null,
                      jobElements: [],
                      logged: null
                    }

        this.inputFile = React.createRef()
        
        this.jobElements = [
            <input type="file" id="job-page-form-file-1" ref={this.inputFile}/>,
            <input type="number" id="job-page-form-arg-1" placeholder="Mes"/>,
            <input type="number" id="job-page-form-arg-2" placeholder="Año"/>
        ]

        this.handleSubmit = this.handleSubmit.bind(this)
    }

    componentDidMount () {
        getJobDataById (this.props.id)
        .then ((res) => {
            this.setState ({jobId: res.data[0].id,
                            jobName: res.data[0].name, 
                            description: res.data[0].description,
                            })
        })

        getSessionUserData ()
        .then ((res) => {
            this.setState ({userName: res.data.username, userId: res.data.id, logged: true})
        })
        .catch((err) => {
            alert(err.response.data.error_message)
            window.location.href = '/login'
        })

        getArgumentsByJobId(this.props.id)
        .then ((res) => {
            let elements = []
            res.data.map((arg, idx) => {
                if (arg.arg_type === "file") {
                    elements.push(<input type={arg.arg_type} id={"job-page-form-file-" + idx.toString()} key={idx} ref={this.inputFile} multiple/>)
                }
                else {
                    elements.push(<input type={arg.arg_type} id={"job-page-form-arg-" + idx.toString()} key={idx} placeholder={arg.placeholder}/>)
                }
                return 0 
            })
            this.setState({jobElements: elements, argCount: res.data.length})
        })
    }

    handleSubmit () {
        console.log (this.state)
        let args = []
        let i
        for (i = 0; i < this.state.argCount - 1; i = i + 1) {
            let id = "job-page-form-arg-" + (i + 1).toString()
            console.log (id)
            let argInput = document.getElementById(id).value
            args.push(argInput)
        }

        let reader = new FileReader()
        reader.readAsText(this.inputFile.current.files[0])
        reader.onload = (e) => {

            let jobData = {
                tagname: this.state.userName + "_" + this.state.jobName,
                job_id: this.state.jobId,
                user_id: this.state.userId,
                filename: this.inputFile.current.files[0].name,
                data: e.target.result,
                arguments: args
            }
            executeJob (jobData)
            window.location.href = "/user"
        }
    }

    render () {
        if (!this.state.logged) {
            return <></>
        }
        else {
            return (
                <>
                    <NavBar elements={navBarElements}/>
                    <PageHeader text={this.state.jobName} id="job-page-header"/>
                    <RegularText text={this.state.description} id="job-page-description"/>
                    <RegularForm action="/user"
                        elements={this.state.jobElements}
                        id="execute-form" 
                        submitText="Ejecutar"
                        submitHandler={this.handleSubmit}
                    />
                    <hr></hr>
                    <RegularLink text="Regresar al inicio" href="/user" id="job-page-home-link"/>
                </>
            )
        }
    }
}

export default JobPage;
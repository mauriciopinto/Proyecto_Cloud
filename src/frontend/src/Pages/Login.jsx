import React from 'react'
import { ImportantButton } from '../Components/Button'
import { PageHeader } from '../Components/Header'
import { RegularForm } from '../Components/Form'
import { postLogin } from '../Services/Account/Login'

let loginFormElements = [
    <input type="text" placeholder="Usuario" id="login-username" key={1}/>,
    <input type="password" placeholder="Contraseña" id="login-password" key={2} />
]

class LoginPage extends React.Component {
    constructor (props) {
        super (props)

        this.state = {}
    }

    render () {
        return (
            <div id="login">
                <PageHeader text="Ingresa los datos de tu cuenta" id="login-header" />
                <RegularForm action="http://localhost:8000/api/login" 
                    elements={loginFormElements} 
                    id="login-form" 
                    submitText="Ingresar"
                    submitHandler={postLogin}
                    //data = {{username: '', password: ''}}
                />
            </div>
        )
    }
}

export default LoginPage
import React from "react"
import { PageHeader } from "../Components/Header"
import { RegularButton, ImportantButton } from "../Components/Button"
import { List } from '../Components/List'
import { RegularLink } from '../Components/Link'
import { NoticeBox } from '../Components/Notice'


let noticeBoxText = "Si aún no tienes acceso a las automatizaciones, contacta a un usuario administrador de tu empresa para que proceda a registrarte"

let sampleListElems = [
    {
        id: "1",
        text: "ala mierda"
    },
    {
        id: "2",
        text: "sapee"
    }
]


class HomePage extends React.Component {
    constructor (props) {
        super (props)
        
        let html_elems = sampleListElems.map((element, i) => {
            return <li id={element.id} key={i}><p>{element.text}</p></li>
        })
        this.state = {listElements: html_elems}
    }

    render () {
        return (
            <div id="home-page">
                <PageHeader text="Automatización de procesos - CONDATA" id="home-header"/>
                <RegularLink text="Ingresar" id="sample-link" href="login/" />
                <NoticeBox text={noticeBoxText} id="home-noticebox" level={1} display={true}/>
            </div>
        )
    }
}

export default HomePage
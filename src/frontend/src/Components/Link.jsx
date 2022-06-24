import React from "react"

let linkStyle = {
    cursor: 'pointer'
}

export class RegularLink extends React.Component {
    constructor (props) {
        super (props)

        this.state = {text: props.text, href: props.href, style: linkStyle}
    }

    render () {
        return (
            <a href={this.state.href} style={this.state.style} id={this.props.id}>{this.state.text}</a>
        )
    }
}
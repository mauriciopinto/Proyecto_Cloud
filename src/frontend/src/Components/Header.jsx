import React from 'react'

export class PageHeader extends React.Component {
    constructor (props) {
        super(props)

        this.state = {text: props.text}
    }

    render () {
        return (
            <h1 id={this.props.id}>{this.props.text}</h1>
        )
    }
}


export class SectionHeader extends React.Component {
    constructor (props) {
        super(props)

        this.state = {text: props.text}
    }
    
    render () {
        return (
            <h2 id={this.props.id}>{this.props.text}</h2>
        )
    }
}
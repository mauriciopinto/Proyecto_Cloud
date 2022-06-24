import React from 'react'

let listStyle = {
    color: "#000000",
    listStyleType: 'none'
}

export class List extends React.Component {
    constructor (props) {
        super (props)

        this.state = {elements: props.elements, style: listStyle}
    }

    render () { 
        return (
            <ul id={this.props.id} style={this.state.style}>
                {this.props.elements}
            </ul>
        )
    }
}
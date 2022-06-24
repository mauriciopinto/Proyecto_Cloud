import React from "react";

export class RegularText extends React.Component {
    constructor (props) {
        super (props)
    }

    render () {
        return (
            <p id={this.props.id}>{this.props.text}</p>
        )
    }
}
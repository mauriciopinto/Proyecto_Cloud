import React from 'react'

/* Regular button colors */ 
var regularButtonBg = "#3498DB"
var regularButtonHighlightedBg = "#AED6F1"

/* Important button colors */
var importantButtonBg = "#2ECC71"
var importantButtonHighlightedBg = "#82E0AA"

/* General Button Style */ 
let regularButtonStyle = {
    padding: '8px',
    border: 'none',
    color: '#ffffff',
    cursor: 'pointer',
    background: regularButtonBg
}

let importantButtonStyle = {
    padding: '8px',
    border: 'none',
    color: '#ffffff',
    cursor: 'pointer',
    background: importantButtonBg
}

export class RegularButton extends React.Component {
    constructor(props) {
        super (props)

        this.state = {text: props.text, style: regularButtonStyle}
        this.handleMouseEnter = this.handleMouseEnter.bind(this)
        this.handleMouseLeave = this.handleMouseLeave.bind(this)
    }

    handleMouseEnter (event) {
        event.target.style.background = regularButtonHighlightedBg
    }

    handleMouseLeave (event) {
        event.target.style.background = regularButtonBg
    }

    render () {
        return (
            <button id={this.props.id} 
                onMouseEnter={this.handleMouseEnter}
                onMouseLeave={this.handleMouseLeave}
                onClick={this.props.onClick}
                style={this.state.style}
                type={this.props.type}
            >
                {this.state.text}
            </button>
        )
    }
}

export class ImportantButton extends React.Component {
    constructor(props) {
        super (props)

        this.state = {text: props.text, style: importantButtonStyle}

        this.handleMouseEnter = this.handleMouseEnter.bind(this)
        this.handleMouseLeave = this.handleMouseLeave.bind(this)
    }
    

    handleMouseEnter (event) {
        event.target.style.background = importantButtonHighlightedBg
    }

    handleMouseLeave (event) {
        event.target.style.background = importantButtonBg
    }

    render () {
        return (
            <button id={this.props.id} 
                onMouseEnter={this.handleMouseEnter}
                onMouseLeave={this.handleMouseLeave} 
                onClick={this.props.onClick}
                style={this.state.style}
                type={this.props.type}
            >
                {this.state.text}
            </button>
        )
    }
}
import React from 'react'

export class NoticeBox extends React.Component {
    constructor (props) {
        super (props)

        this.state = {text: props.text, level: props.level, style: null}
    }

    render () {
        let bg = ''
        let color = ''
        if (this.state.level == 1) {
            bg = '#D6EAF8'
            color = '#5DADE2'
        }

        else if (this.state.level == 2) {
            bg = '#FCF3CF'
            color = '#F1C40F'
        }

        else if (this.state.level == 3) {
            bg = '#FADBD8'
            color = '#EC7063'
        }
        
        let style = null
        if (this.props.display) {
            style = { 
                padding: '8px',
                background: bg,
                color: color
            }
        }
        else {
            style = {
                padding: '8px',
                background: bg,
                color: color,
                display: 'none'
            }
        }
        return (
            <div id={this.props.id} style={style}>
                {this.props.text}
            </div>
        )
    }
}
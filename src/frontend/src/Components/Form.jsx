import React from 'react'
import { ImportantButton } from './Button'
import { NoticeBox } from './Notice'

let formStyle = {
    color: '#000000'
}

export class RegularForm extends React.Component {
    constructor (props) {
        super (props)

        this.state = {
                        action: props.action, 
                        elements: props.elements, 
                        style: formStyle,
                        data: props.data,
                        noticeDisplay: false,
                        noticeText: ''
                    }
        this.submitHandler = props.submitHandler
        this.file = React.createRef ()
    }


    render () {
        return (
            <form 
                action={this.props.action}
                id={this.props.id} 
                onSubmit={(event) => {
                    event.preventDefault() 
                    this.submitHandler (event, (res) => {
                        this.setState({noticeDisplay: true, noticeText: res.data.error_message})})
                }}
            >
                {this.props.elements}
                <ImportantButton text={this.props.submitText} id="login-submit" type="submit" />
                <NoticeBox text={this.state.noticeText} level={3} id={this.props.id + "-notice"} display={this.state.noticeDisplay} />
            </form>
        )
    }
}
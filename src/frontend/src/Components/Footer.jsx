import React from 'react'

class Footer extends React.Component {
    constructor(props) {
        super (props)

        this.state = {elements: this.props.elements}
    }

    render () {
        return (
            <footer>
                {this.state.elements}
            </footer>
        )
    }
}

export default Footer;
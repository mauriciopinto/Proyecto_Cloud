import React from 'react'

class NavBar extends React.Component {
    constructor(props) {
        super (props)

        this.state = {elements: props.elements}
    }

    render () {
        return (
            <nav>
                {this.state.elements.map((item) => {
                    return <><a href={item.link}>{item.text}</a> | </>
                })}
            </nav>
        )
    }
}

export default NavBar;
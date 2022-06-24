import React from 'react'

export class RegularTable extends React.Component {
    constructor (props) {
        super (props)
    }

    render () {
        return (
            <table>
                <thead>
                    <tr>
                        {
                            this.props.headers.map((h) => {
                                return <th>{h}</th>
                            })
                        }
                    </tr>
                </thead>
                <br />
                <tbody>
                    {this.props.elements}
                </tbody>
            </table>
        )
    }
}
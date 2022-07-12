import axios from "axios"

let CONDATA_API_URL = "http://192.168.59.117:32647/api/"

export function postLogin (event, renderResponse) {
    
    
    let url = CONDATA_API_URL + "login/"
    let response = null
    let formData = new FormData()
    formData.append("username", event.target[0].value)
    formData.append("password", event.target[1].value)
    
    response = axios.post (url, formData, {withCredentials: true})
    .then (res => {
        if (res.status === 200) {
            window.location.href = '/user'
        }
    })
    .catch ((err) => {
        renderResponse(err.response)
    })
}

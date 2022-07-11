import axios from 'axios'

let CONDATA_API_URL = "http://192.168.59.100:32647/api/"

export function getSessionUserData () {
    let requestData = {
        withCredentials: true
    }
    let url = CONDATA_API_URL + 'session/'

    return axios.get(url, requestData)
}

export function closeUserSession () {
    let requestData = {
        withCredentials: true
    }
    let url = CONDATA_API_URL + 'logout/'
    
    return axios.get(url, requestData)
}

export function getUserData (id) {
    let requestData = {
        withCredentials: true
    }
    let url = CONDATA_API_URL + 'users/' + id

    return axios.get(url, requestData)
}

export function getJobsByClientId (clientId) {
    let url = CONDATA_API_URL + 'jobs/?client_id=' + clientId

    return axios.get(url)
}

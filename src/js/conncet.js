import axios from 'axios'


const http = axios.create({
    baseURL: 'http://114.132.247.238:5000',
})
export default http
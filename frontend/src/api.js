import axios from 'axios'
import { ACCESS_TOKEN } from './constants'

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
    //this base url, it imports the backend url from .env 
})

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    }, 
    (error) => {
        return Promise.reject(error)
    }
)

export default api
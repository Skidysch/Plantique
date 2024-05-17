import axios from "axios";

const instance = axios.create({
  baseURL: "http://localhost:5173/api/v1",
  headers: {
    "Content-Type": "application/json",
    "Accept": "application/json",
  },
})

export default instance;
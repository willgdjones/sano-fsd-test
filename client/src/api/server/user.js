import axios from "axios";

export function join(study_key) {
    return new Promise((resolve, reject) => {
        axios
            .post(`/user/enrollment/${study_key}`)
            .then((response) => {
                resolve(response);
            })
            .catch((error) => {
                reject(error);
            });
    });
}

export function leave(study_key) {
    return new Promise((resolve, reject) => {
        axios
            .delete(`/user/enrollment/${study_key}`)
            .then((response) => {
                resolve(response);
            })
            .catch((error) => {
                reject(error);
            });
    });
}

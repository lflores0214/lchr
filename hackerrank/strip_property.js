function stripProperty(obj, prop) {
    if (obj.hasOwnProperty(prop)) {
        delete obj[prop]
    } else {
        return {}
    }
}

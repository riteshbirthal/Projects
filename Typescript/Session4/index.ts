

setTimeout(()=>{
    console.log("hello");
}, 2000);

const demo = () => {
    return new Promise((resolve, reject) =>{
        resolve(true);
    }).catch((err)=>console.log(err));
};

demo().then((data)=>{
    console.log(data);
}).catch((err) => console.log(err));
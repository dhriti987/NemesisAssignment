const body = document.getElementById("tableBody");
const popUp = document.querySelector(".editPopUp");
const a = [
  {
    id: 1,
    email: "hello@gmail.com",
    name: "nitin",
    address: "noAddress",
  },
  {
    id: 2,
    email: "hello@gmail.com",
    name: "nitin",
    address: "noAddress",
  },
  {
    id: 3,
    email: "hello@gmail.com",
    name: "nitin",
    address: "noAddress",
  },
];

const fetchUser = async () => {
  // try{
  const response = await fetch("http://127.0.0.1:8000/user/user",{
    method: 'GET',
    headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Methods": "GET,HEAD,OPTIONS,POST,PUT",
        "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept, Authorization"
      }
  });
  // console.log("d")
//   const data = await response.json();
  console.log(response);
  // }
  // catch(err){
  // console.log(err.message);
  // }
};
fetchUser();

const editFunc = (id, name, email, address) => {
  console.log(popUp);
  document.getElementById("editEmail").value = email;
  document.getElementById("editName").value = name;
  document.getElementById("editAddress").value = address;
  popUp.style.display = "block";
};

a.forEach((item) => {
  const tr = document.createElement("tr");
  const td1 = document.createElement("td");
  const td2 = document.createElement("td");
  const td3 = document.createElement("td");
  const td4 = document.createElement("td");
  const td5 = document.createElement("td");
  const btn1 = document.createElement("button");
  const btn2 = document.createElement("button");
  btn1.append(document.createTextNode("Edit"));
  btn1.classList.add("btn", "btn-primary");
  btn2.append(document.createTextNode("Delete"));
  btn2.classList.add("btn", "btn-primary");
  td1.style.width = "20%";
  td2.style.width = "20%";
  td4.style.width = "0";
  td5.style.width = "0";
  td1.appendChild(document.createTextNode(`${item.email}`));
  td2.appendChild(document.createTextNode(`${item.name}`));
  td3.appendChild(document.createTextNode(`${item.address}`));
  td4.appendChild(btn1);
  td5.appendChild(btn2);
  tr.appendChild(td1);
  tr.appendChild(td2);
  tr.appendChild(td3);
  tr.appendChild(td4);
  tr.appendChild(td5);
  btn1.addEventListener("click", () =>
    editFunc(item.id, item.name, item.email, item.address)
  );
  body.appendChild(tr);
});

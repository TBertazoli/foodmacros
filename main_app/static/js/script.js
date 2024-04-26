// require("dotenv").config();

// const app_key = process.env.APPLICATION_KEY;
// const app_id = process.env.APPLICATION_ID;

// const url =
//   "https://api.edamam.com/api/food-database/v2/parser?app_id=" +
//   app_key +
//   "&app_key=" +
//   app_id +
//   "&ingr=rice&nutrition-type=cooking";

// export async function getFoodData() {
//   const response = await fetch(url, {
//     method: "GET",
//     headers: {
//       "Content-Type": "application/json",
//       "X-CSRFToken": csrftoken,
//     },
//     body: JSON.stringify({ data })
//       .then((result) => {
//         console.log(result);
//       })
//       .catch((err) => {
//         console.log(err);
//       }),
//   });
// }

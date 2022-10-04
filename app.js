const express = require("express");
const mysql = require("mysql2");
const app = express();
const bodyParser = require("body-parser");
const port = 3100;

const connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "test",
});

//
app.use(bodyParser.json());

// CREATE(insert)
app.post("/users", (req, res) => {
  const { tupid, firstname,lastname,phone,address,email } = req.body;

  connection.query(
    "INSERT INTO users (tupid,firstname,lastname,phone,address,email) VALUES (?,?,?,?,?,?)",
    [tupid, firstname,lastname,phone,address,email],
    (err, results) => {
      try {
        if (results.affectedRows > 0) {
          res.json({ message: "Data has been added!" });
        } else {
          res.json({ message: "Something went wrong." });
        }
      } catch (err) {
        res.json({ message: err });
      }
    }
  );
});

// READ (select)
app.get("/users", (req, res) => {
  connection.query("SELECT * FROM users", (err, results) => {
    try {
      if (results.length > 0) {
        res.json(results);
      }
    } catch (err) {
      res.json({ message: err });
    }
  });
});

// UPDATE (update)
app.put("/users", (req, res) => {
  const { lastname, address,tupid } = req.body;

  if (tupid && lastname && address) {
    connection.query(
      "UPDATE users SET lastname = ?, address = ? WHERE tupid = ?",
      [lastname, address,tupid],
      (err, results) => {
        try {
          if (results.affectedRows > 0) {
            res.json({ message: "Data has been updated!" });
          } else {
            res.json({ message: "Something went wrong." });
          }
        } catch (err) {
          res.json({ message: err });
        }
      }
    );
  } else if (tupid && lastname) {
    connection.query(
      "UPDATE users SET lastname = ? WHERE tupid = ?",
      [lastname, tupid],
      (err, results) => {
        try {
          if (results.affectedRows > 0) {
            res.json({ message: "Data has been updated!" });
          } else {
            res.json({ message: "Something went wrong." });
          }
        } catch (err) {
          res.json({ message: err });
        }
      }
    );
  }
});

// DELETE
app.delete("/users", (req, res) => {
  const { tupid } = req.body;

  connection.query("DELETE FROM users WHERE tupid = ?", [tupid], (err, results) => {
    try {
      if (results.affectedRows > 0) {
        res.json({ message: "Data has been deleted!" });
      } else {
        res.json({ message: "Something went wrong." });
      }
    } catch (err) {
      res.json({ message: err });
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
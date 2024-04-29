const express = require("express");

const port = process.env.PORT || 3005;

const app = express();

app.set("view engine", "ejs");

app.use(express.urlencoded({ extended: false }));

app.get("/", (req, res) => {
  res.render("home");
});

app.use((req, res, next) => {
  // Breadcrumbs data
  const fullUrl = req.protocol + "://" + req.get("host") + req.originalUrl;
  const folders = new URL(fullUrl).pathname.split("/").slice(1);
  const breadcrumbs = folders.map(
    (folder) => folder.charAt(0).toUpperCase() + folder.slice(1)
  );

  // Pass breadcrumbs data to all views
  res.locals.breadcrumbs = breadcrumbs;

  next();
});

// Accessories
app.get("/accessories", (req, res) => {
  res.render("accessories", {
    fullUrl: req.protocol + "://" + req.get("host") + "/accessories",
  });
});

app.get("/accessories/keyboards", (req, res) => {
  res.render("keyboards", {
    fullUrl: req.protocol + "://" + req.get("host") + "/accessories/keyboards",
  });
});

app.get("/accessories/mice", (req, res) => {
  res.render("mice", {
    fullUrl: req.protocol + "://" + req.get("host") + "/accessories/mice",
  });
});

// Computers
app.get("/computers/", (req, res) => {
  res.render("computers", {
    fullUrl: req.protocol + "://" + req.get("host") + "/computers/",
  });
});

app.get("/computers/laptops", (req, res) => {
  res.render("laptops", {
    fullUrl: req.protocol + "://" + req.get("host") + "/computers/laptops",
  });
});

app.get("/computers/laptops/macs", (req, res) => {
  res.render("macs", {
    fullUrl: req.protocol + "://" + req.get("host") + "/computers/laptops/macs",
  });
});

app.get("/computers/laptops/windows", (req, res) => {
  res.render("windows", {
    fullUrl:
      req.protocol + "://" + req.get("host") + "/computers/laptops/windows",
  });
});

app.get("/computers/desktops/macs", (req, res) => {
  res.render("macs", {
    fullUrl:
      req.protocol + "://" + req.get("host") + "/computers/desktops/macs",
  });
});

app.get("/computers/desktops/pcs", (req, res) => {
  res.render("pcs", {
    fullUrl: req.protocol + "://" + req.get("host") + "/computers/desktops/pcs",
  });
});

app.get("/computers/desktops", (req, res) => {
  res.render("desktops", {
    fullUrl: req.protocol + "://" + req.get("host") + "/computers/desktops",
  });
});

app.get("/surveyStart", (req, res) => {
  var missingFields = req.param.invalid;
  if (missingFields) {
    res.render("survey", { missingFields: 1 });
  } else {
    res.render("survey");
  }
});

app.post("/submitSurvey", (req, res) => {
  var phoneType = req.body.phoneType;
  var email = req.body.email;

  if (!email || !phoneType) {
    return res.render("survey", { invalid: true });
  }

  var phoneStats = {
    iphone: 57,
    android: 43,
  }; //stats according to statista.com for Canada 2022 (https://www.statista.com/statistics/1190552/smartphone-market-share-canada/)

  var percent = 0;
  if (phoneType === "iphone") {
    percent = phoneStats.iphone;
  } else if (phoneType === "android") {
    percent = phoneStats.android;
  }

  res.render("surveyResults", { percent: percent, usersPhoneType: phoneType });
});

app.listen(port, () => {
  console.log("Node application listening on port " + port);
});

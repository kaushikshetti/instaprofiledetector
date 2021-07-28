function validateForm() {
  var a = document.forms["passdata"]["userfollowercount"].value;
  var b = document.forms["passdata"]["userfollowingcount"].value;
  var c = document.forms["passdata"]["userbiographylength"].value;
  var d = document.forms["passdata"]["usermediacount"].value;
  var e = document.forms["passdata"]["userhasprofilepic"].value;
  var f = document.forms["passdata"]["userisprivate"].value;
  var g = document.forms["passdata"]["usernamedigitcount"].value;
  var h = document.forms["passdata"]["usernamelength"].value;

  if (a == "") {
    alert("User Follower Count must be filled out.");
    return false;
  }
  if (b == "") {
    alert("User Following Count must be filled out.");
    return false;
  }
  if (c == "") {
    alert("User Biography Length must be filled out.");
    return false;
  }
  if (d == "") {
    alert("User Media Count must be filled out.");
    return false;
  }
  if (e == "") {
    alert("User has a Profile Picture must be filled out.");
    return false;
  }
  if (f == "") {
    alert("User is Private must be filled out.");
    return false;
  }
  if (g == "") {
    alert("Username Digitcount must be filled out.");
    return false;
  }
  if (h == "") {
    alert("Username Length must be filled out.");
    return false;
  }
}
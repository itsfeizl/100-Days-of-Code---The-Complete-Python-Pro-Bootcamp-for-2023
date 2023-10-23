function toggleSummary(headline) {
  var dropdownContent = headline.getElementsByClassName("dropdown-content")[0];
  var isOpen = dropdownContent.style.display === "block";

  // Close all open dropdowns except the clicked one
  var openHeadlines = document.getElementsByClassName("headline open");
  for (var i = 0; i < openHeadlines.length; i++) {
    if (openHeadlines[i] !== headline) {
      var openDropdownContent =
        openHeadlines[i].getElementsByClassName("dropdown-content")[0];
      openDropdownContent.style.display = "none";
      openHeadlines[i].classList.remove("open");
    }
  }

  // Check if the clicked element is an <a> tag
  if (event.target.tagName.toLowerCase() !== "a") {
    // Toggle the clicked dropdown
    if (isOpen) {
      dropdownContent.style.display = "none";
      headline.classList.remove("open");
      headline.classList.remove("space");
    } else {
      dropdownContent.style.display = "block";
      headline.classList.add("open");
      headline.classList.add("space");
    }

    // Prevent the default behavior of the click event
    event.preventDefault();
  }
}

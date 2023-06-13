from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as my_file:
    content = my_file.read()

# Parse the contents of a html site and save it into a variable
website_soup = BeautifulSoup(content, "html.parser")
# print(website_soup.prettify()) # The .prettify() formats the output


# Get the <title> element from the website with .title
# .title returns the title element - the tags as well as the string within the tags <title>String</title>
website_soup_title = website_soup.title


# Use .name to get only the tag name without the entire element
website_soup_title_name = website_soup_title.name


# Use .string to get only the string (text) within the element without the entire element
website_soup_title_string = website_soup_title.string


# Get the first <a> element from the site
# Use the .string method to get only the text
website_soup_anchor = website_soup.a
print(website_soup_anchor.string)


# Get the first <li> element from the site
# Use the .string method to get only the text
website_soup_list = website_soup.li
print(website_soup_list.string)


# Get all the elements within the site with the find_all() method.
# The method returns all the elements passed to it with the 'name' parameter stored in a list
all_anchor_elements = website_soup.find_all(name="a")
print(all_anchor_elements)

all_list_elements = website_soup.find_all(name="li")
print(all_list_elements)

all_paragraph_elements = website_soup.find_all(name="p")
print(all_paragraph_elements)


# Use the .getText() (similar to .string) method to get the text within an element
# The .get() method will return the attribute passed to it, in this example the "href"
for tag in all_anchor_elements:
    print(tag.getText())
    print(tag.get("href"))
    print()


# Print a h1 element with the id: name
print(website_soup.find(name="h1", id="name"))

# Print a h3 element with the class: heading
print(website_soup.find(name="h3", class_="heading"))


# Print an <a> element that sits within a <p> element
print(website_soup.select_one(selector="p a"))

# .select_one with id name
print(website_soup.select_one(selector="#name"))

# .select_one with class name
print(website_soup.select_one(selector=".heading"))
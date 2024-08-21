from bs4 import BeautifulSoup

# Load the HTML content
with open('index2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Open the output file for writing
with open('output.txt', 'w', encoding='utf-8') as output_file:
    # Find all the rows in the table
    rows = soup.find_all('tr')

    for row in rows:
        # Find the problem ID in the modal content
        problem_id_modal = row.find('div', class_='modal-body')
        if problem_id_modal:
            problem_id = problem_id_modal.find('div', class_='style-2').text.strip()
        else:
            continue  # Skip this row if no problem ID is found

        # Find the organization
        organization = row.find_all('td', class_='colomn_border')[1].text.strip()

        # Find the problem title in the modal content
        problem_title_modal = row.find('a', {'data-toggle': 'modal'})
        if problem_title_modal:
            problem_title = problem_title_modal.text.strip()
        else:
            continue  # Skip this row if no problem title is found

        # Find the problem description in the modal content
        problem_description_modal = problem_id_modal.find_all('div', class_='style-2')[2].text.strip()

        # Write to the output file
        output_file.write(f"Problem ID: {problem_id}\n")
        output_file.write(f"Organization: {organization}\n")
        output_file.write(f"Title: {problem_title}\n")
        output_file.write(f"Description: {problem_description_modal}\n")
        output_file.write("\n" + "-"*40 + "\n\n")

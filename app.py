import fitz

doc = fitz.open("2024_Rookie_Scouting_Portfolio (1).pdf") # open a document
out = open("output_solid_RSP_wr.txt", "wb") # create a text output
start_page = 244
end_page = 279

with open("output_RSP_wr.txt", "w") as output_file:

 for page_number in range(start_page, end_page):
        page = doc[page_number]  # Access the page
        text = page.get_text("text")  # Extract text from the page
        
        # Write the text to the output file
        output_file.write(f"Text from page {page_number + 1}:\n")
        output_file.write(text)
        output_file.write("\n\n") 
doc.close()
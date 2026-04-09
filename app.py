import gradio as gr


#makes the numbers and colors the current pair red
def visualList(arr, o):
    if not arr: #if array empty then return nothing
        return ""
    #AI helped with the proper font sizes and coloration. Originally I used highlight, but that did not work as intended so AI debugged to use html as a smoother alternative
    html = "<div style='font-size: 24px; font-family: sans-serif; letter-spacing: 8px;'>" #font for visual
    for index, x in enumerate(arr): #go through each number to check for numbers being sorted
        #if its the nums being sorted then turn color red, else do nothing
        if index == o or index == o + 1:
            html += f"<span style='color: red; font-weight: bold;'>{x}</span> "
        else:
            html += f"<span>{x}</span> "
    return html + "</div>"


#swaps numbers when clicking and performs bubblesort
def bubblesort(numbers, i, o):
    if not numbers: #when no list is entered to be sorted
        return numbers, i, o, "Please enter numbers first", "error"

    #stops if all sorts is done
    if i >= len(numbers) - 1:
        return numbers, i, o, visualList(numbers, -2), "All sorted!"

    sortLine = f"Comparing {numbers[o]} and {numbers[o + 1]}"

    #bubble sort
    if numbers[o] > numbers[o + 1]: #if the number beside is larger then swap positions
        temp = numbers[o] #temp variable to swap positions
        numbers[o] =  numbers[o + 1]
        numbers[o + 1] = temp
        sortLine += f" -> swapped since {numbers[o]} > {numbers[o + 1]}!"
    else:
        sortLine += f" -> no swap since {numbers[o]} < {numbers[o + 1]}!."

    current_view = visualList(numbers, o)

    #increment o for next numbers to be sorted
    o += 1

    #if o hits end of list, go back and increment i
    if o >= len(numbers) - 1 - i:
        o = 0
        i += 1
        sortLine += " (End reached, going back to start)"

    return numbers, i, o, current_view, sortLine


#text input and the counter
def loadList(input_str):
    try: #use try and else so that it will run always
        #turn string into list of ints
        #AI helped me debug this, originally multiple "," caused an error. But then AI suggested I use the strip function
        new_list = [int(x.strip()) for x in input_str.split(",") if x.strip()] #use strip to remove extra commas
        #Return list, reset i=0, reset o=0, visualize it, and updates list
        return new_list, 0, 0, visualList(new_list, 0), "List loaded. Click next to start."
    except: #if a list in loaded improperly
        return [], 0, 0, "Error", "Please use numbers like: 1, 2, 3"


#UI function
with gr.Blocks() as demo:
    #starting default list
    defaultList = [5, 10, 1, 4, 3, 2, 6, 7, 8, 9, 12, 11]

    # states keep track of your place in the list
    listState = gr.State(defaultList)
    iState = gr.State(0)
    oState = gr.State(0)

    gr.Markdown("# BubbleSort: frame by frame")

    #get user inputs
    with gr.Row():
        userInput = gr.Textbox(
            label="Input numbers (comma separated)",
            value="5, 10, 1, 4, 3, 2, 6, 7, 8, 9, 12, 11"
        )
        set_btn = gr.Button("set/reset list")

    #Displays for buttons
    out_html = gr.HTML(value=visualList(defaultList, 0))
    status = gr.Textbox(label="What happened", value="Click next step to start")

    #Button to go to next sort step
    btn = gr.Button("Next step ➡", variant="primary")

    #Button to get user inputs
    set_btn.click(
        loadList,
        inputs=userInput,
        outputs=[listState, iState, oState, out_html, status]
    )

    #Button to sort the list
    btn.click(
        bubblesort,
        inputs=[listState, iState, oState],
        outputs=[listState, iState, oState, out_html, status]
    )

demo.launch()
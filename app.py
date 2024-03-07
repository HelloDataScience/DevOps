import logging

logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)

def server(input, output, session):
    logging.info("App start")

    @reactive.Calc
    def vals():
        d = {
            "bill_length_mm" : input.bill_length(),
            "sex_male" : input.sex() == "Male",
            "species_Gentoo" : input.species() == "Gentoo", 
            "species_Chinstrap" : input.species() == "Chinstrap"

        }
        return d
    
    @reactive.Calc
    @reactive.event(input.predict)
    def pred():
        logging.info("Request Made")
        r = requests.post(api_url, json = [vals()])
        logging.info("Request Returned")

        if r.status_code != 200:
            logging.error("HTTP error returned")

        return r.json().get('predict')[0]

    @output
    @render.text
    def vals_out():
        return f"{vals()}"

    @output
    @render.text
    def pred_out():
        return f"{round(pred())}"

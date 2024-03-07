server <- function(input, output) {
  log <- log4r::logger()
  log4r::info(log, "App Started")
  # Input params
  vals <- reactive(
    list(
      bill_length_mm = input$bill_length,
      species_Chinstrap = input$species == "Chinstrap",
      species_Gentoo = input$species == "Gentoo",
      sex_male = input$sex == "Male"
    )
  )
  
  # Fetch prediction from API
  pred <- eventReactive(
    input$predict,
    {
      log4r::info(log, "Prediction Requested")
      r <- httr2::request(api_url) |>
        httr2::req_body_json(list(vals())) |>
        httr2::req_perform()
      log4r::info(log, "Prediction Returned")
      
      if (httr2::resp_is_error(r)) {
        log4r::error(log, paste("HTTP Error"))
      }
      
      httr2::resp_body_json(r)
    },
    ignoreInit = TRUE
  )
  
  # Render to UI
  output$pred <- renderText(pred()$predict[[1]])
  output$vals <- renderPrint(vals())
}

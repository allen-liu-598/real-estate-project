from fastapi import FastAPI
import gradio as gr
from gradio.routes import mount_gradio_app

from .utils.prediction import predictPrice

app = FastAPI()
    
def gradio_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# Real Estate Price Estimator")
    
        with gr.Row():
            lot_area = gr.Number(label="Lot Area (sqft)")
            quality = gr.Number(label="Overall Quality (1-10)")
            condition = gr.Number(label="Overall Condition (1-10)")
            central_air = gr.Checkbox(label="Central Air")
            full_bath = gr.Number(label="Full Bathrooms")
            bedrooms = gr.Number(label="Bedrooms")
            garage_cars = gr.Number(label="Garage Cars")

        predict_button = gr.Button("Predict Price")
        output = gr.Textbox(label="Estimated Sale Price")

        predict_button.click(
            fn=predictPrice,
            inputs=[lot_area, quality, condition, central_air, full_bath, bedrooms, garage_cars],
            outputs=[output],
        )
    return demo

gradio_app = gradio_interface()
mount_gradio_app(app, gradio_app, path="/")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
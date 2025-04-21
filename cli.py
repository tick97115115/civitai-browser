import typer
import sys
# sys.path.append(".")  # Adjust the path to your project structure
app = typer.Typer()

@app.command()
def testdatamodel():
    """
    Test the data model.
    """
    from data_analysis.data_model_validation import validate_data
    validate_data()
    typer.echo("Data model is valid.")

if __name__ == "__main__":
    app()
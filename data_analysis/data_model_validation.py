from api.v1.models.civitai_model import CivitAI_ModelId
from data_analysis.main import engine, ApiInfo
from sqlmodel import Session, select

def validate_data():
    with Session(engine) as session:
        # 这里可以添加一些测试代码
        statement = select(ApiInfo)
        results = session.exec(statement)
        for item in results:
            try:
                model = CivitAI_ModelId.model_validate(item.api_info_json)
            except Exception as e:
                print(f"Error validating model: {e}")
                continue

if __name__ == "__main__":
    validate_data()
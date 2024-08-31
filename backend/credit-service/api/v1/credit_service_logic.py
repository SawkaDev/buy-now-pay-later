# credit_service.py

from sqlalchemy.exc import SQLAlchemyError
from models.credit import CreditProfile
from sqlalchemy.orm import joinedload
from uuid import uuid4

class CreditService:
    def __init__(self, db_session):
        self.db = db_session

    def create_credit_profile(self, name: str, credit_score: int, 
                              number_of_accounts: int, credit_utilization_ratio: float, 
                              recent_soft_inquiries: int, bankruptcies: int, 
                              tax_liens: int, judgments: int) -> CreditProfile:
        try:
            new_profile = CreditProfile(
                id=str(uuid4()),
                user_id=str(uuid4()),
                name=name,
                credit_score=credit_score,
                number_of_accounts=number_of_accounts,
                credit_utilization_ratio=credit_utilization_ratio,
                recent_soft_inquiries=recent_soft_inquiries,
                bankruptcies=bankruptcies,
                tax_liens=tax_liens,
                judgments=judgments
            )
            self.db.add(new_profile)
            self.db.commit()
            return new_profile
        except SQLAlchemyError as e:
            self.db.rollback()
            raise RuntimeError(f"Database error occurred: {str(e)}")

    # def get_credit_profile(self, user_id: str) -> CreditProfile:
    #     profile = self.db.query(CreditProfile).filter(CreditProfile.user_id == user_id).first()
    #     if not profile:
    #         raise LookupError(f"Credit profile for user {user_id} not found")
    #     return profile

    # def update_credit_profile(self, user_id: str, **kwargs) -> CreditProfile:
    #     profile = self.get_credit_profile(user_id)
    #     for key, value in kwargs.items():
    #         if hasattr(profile, key):
    #             setattr(profile, key, value)
    #         else:
    #             raise ValueError(f"Invalid attribute: {key}")
        
    #     try:
    #         self.db.commit()
    #         return profile
    #     except SQLAlchemyError as e:
    #         self.db.rollback()
    #         raise RuntimeError(f"Database error occurred: {str(e)}")

    # def delete_credit_profile(self, user_id: str) -> bool:
    #     profile = self.get_credit_profile(user_id)
    #     try:
    #         self.db.delete(profile)
    #         self.db.commit()
    #         return True
    #     except SQLAlchemyError as e:
    #         self.db.rollback()
    #         raise RuntimeError(f"Database error occurred: {str(e)}")

    # def get_credit_score(self, user_id: str) -> int:
    #     profile = self.get_credit_profile(user_id)
    #     return profile.credit_score

    # def update_credit_score(self, user_id: str, new_score: int) -> CreditProfile:
    #     return self.update_credit_profile(user_id, credit_score=new_score)

    # def calculate_credit_risk(self, user_id: str) -> str:
    #     profile = self.get_credit_profile(user_id)
    #     score = profile.credit_score
    #     if score >= 750:
    #         return "Low"
    #     elif 650 <= score < 750:
    #         return "Medium"
    #     else:
    #         return "High"

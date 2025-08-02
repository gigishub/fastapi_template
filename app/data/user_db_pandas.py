import pandas as pd
import os
from typing import Optional
import uuid

CSV_PATH = os.path.join(os.path.dirname(__file__), "users.csv")

class UserDb:
    """
    Handles loading and saving user data using pandas and CSV.
    """

    @classmethod
    def load_users(cls) -> pd.DataFrame:
        """
        Load users from CSV. If file doesn't exist, return empty DataFrame with expected columns.
        """
        if os.path.exists(CSV_PATH):
            return pd.read_csv(CSV_PATH)
        else:
            return pd.DataFrame(columns=[
                "user_id", "username", "email", "password",
                "session_key", "last_login", "last_logout"
            ])

    @classmethod
    def save_users(cls, df: pd.DataFrame) -> None:
        """
        Save the users DataFrame to CSV.
        """
        df.to_csv(CSV_PATH, index=False)

    @classmethod
    def gen_new_user_id(cls) -> str:
        """
        Generate a new unique user ID as a string (UUID4).
        Returns:
            str: A unique user ID.
        """
        return str(uuid.uuid4())

    @classmethod
    def get_user_by_email(cls, email: str) -> Optional[dict]:
        """
        Get user by email address.
        """
        df = cls.load_users()
        user_row = df[df["email"] == email]
        if not user_row.empty:
            return user_row.iloc[0].to_dict()
        return None

    @classmethod
    def get_user_by_username(cls, username: str) -> Optional[dict]:
        """
        Get user by username.
        """
        df = cls.load_users()
        user_row = df[df["username"] == username]
        if not user_row.empty:
            return user_row.iloc[0].to_dict()
        return None

    @classmethod
    def update_user_session(cls, username: str, session_key: str, login_time: str) -> None:
        """
        Update session key and last_login time for a user.
        """
        df = cls.load_users()
        idx = df.index[df["username"] == username]
        if not idx.empty:
            df.loc[idx, "session_key"] = session_key
            df.loc[idx, "last_login"] = login_time
            cls.save_users(df)

    @classmethod
    def clear_user_session(cls, username: str, logout_time: str) -> None:
        """
        Clear session key and set last_logout time for a user.
        """
        df = cls.load_users()
        idx = df.index[df["username"] == username]
        if not idx.empty:
            df.loc[idx, "session_key"] = ""
            df.loc[idx, "last_logout"] = logout_time
            cls.save_users(df)

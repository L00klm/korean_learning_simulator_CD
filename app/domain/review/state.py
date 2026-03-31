"""주간 복습 그래프용 상태 스키마."""

# from typing import TypedDict 추후 필요 시 추가

from app.domain.shared.state import BaseState


class ReviewState(BaseState, total=False):
    """퀴즈와 플래시카드 생성을 위한 복습 상태."""

    selected_weak_sessions: list[dict]
    chosung_quiz: list[dict]
    flashcards: list[dict]

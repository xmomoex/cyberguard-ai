from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user

from app.schemas.scan_schema import ScanRequest
from app.models.scan import Scan

from app.services.url_scanner import basic_url_analysis
from app.services.ai_service import generate_ai_explanation

router = APIRouter(
    prefix="/scan",
    tags=["Scanner AI"]
)


# -----------------------------------
# CREATE SCAN
# -----------------------------------
@router.post("/url")
def scan_url(
    request: ScanRequest,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    analysis = basic_url_analysis(request.url)

    ai_text = generate_ai_explanation(
        request.url,
        analysis
    )

    scan = Scan(
        url=request.url,
        result=analysis["risk"],
        risk_score=analysis["score"],
        ai_explanation=ai_text,
        user_id=user.id
    )

    db.add(scan)
    db.commit()
    db.refresh(scan)

    return {
        "id": scan.id,
        "url": request.url,
        "risk": analysis["risk"],
        "score": analysis["score"],
        "reasons": analysis["reasons"],
        "ai_explanation": ai_text
    }


# -----------------------------------
# GET HISTORY
# -----------------------------------
@router.get("/history")
def get_scan_history(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    scans = db.query(Scan).filter(
        Scan.user_id == user.id
    ).all()

    return scans


# -----------------------------------
# GET ONE SCAN
# -----------------------------------
@router.get("/{scan_id}")
def get_scan(
    scan_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    scan = db.query(Scan).filter(
        Scan.id == scan_id,
        Scan.user_id == user.id
    ).first()

    if not scan:
        raise HTTPException(
            status_code=404,
            detail="Scan not found"
        )

    return scan


# -----------------------------------
# DELETE SCAN
# -----------------------------------
@router.delete("/{scan_id}")
def delete_scan(
    scan_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    scan = db.query(Scan).filter(
        Scan.id == scan_id,
        Scan.user_id == user.id
    ).first()

    if not scan:
        raise HTTPException(
            status_code=404,
            detail="Scan not found"
        )

    db.delete(scan)
    db.commit()

    return {
        "message": "Scan deleted successfully"
    }
from db.database import get_db
from models.incident import Incident
#from core.security import get_current_user
from sqlalchemy.orm import Session

def create_incident(db: Session, incident_data):
    new_incident = Incident(
        description=incident_data.description,
        type=incident_data.type,
        region=incident_data.region,
        location=incident_data.location,
        photo_url=incident_data.image_url,
        #user_id=current_user.id
    )
    db.add(new_incident)
    db.commit()
    db.refresh(new_incident)
    return new_incident
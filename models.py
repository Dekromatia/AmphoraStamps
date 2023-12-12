from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, create_engine, Column, Text, CHAR, VARCHAR, Date, Integer, String, SmallInteger, Numeric, Unicode, UnicodeText

db = SQLAlchemy()

class Site(db.Model):
    __tablename__ = 'site'
    id = db.Column(db.SmallInteger, primary_key=True)
    site_name = db.Column(db.VARCHAR(150), nullable=False)
    site_latitude = db.Column(db.Numeric (precision=7, scale=5))
    site_longitude = db.Column(db.Numeric (precision=7, scale=5))
    # Определение модели Site

class Manufact(db.Model):
    __tablename__ = 'manufact'
    id = db.Column(db.SmallInteger, primary_key=True)
    manufact_center = db.Column(db.VARCHAR(150), nullable=False)
    manufact_latitude = db.Column(db.Numeric (precision=7, scale=5))
    manufact_longitude = db.Column(db.Numeric (precision=7, scale=5))
    # Определение модели Manufact

class Artifact(db.Model):
    __tablename__ = 'artifact'
    id = db.Column(db.SmallInteger, primary_key=True)
    site_id = db.Column(db.SmallInteger, db.ForeignKey('site.id'))
    manufact_id = db.Column(db.SmallInteger, db.ForeignKey('manufact.id'))
    year_exc = db.Column(db.VARCHAR(20))
    unit_exc = db.Column(db.VARCHAR(150))
    leader_exc = db.Column(db.VARCHAR(150))
    artif_position = db.Column(db.VARCHAR(15))
    field_id = db.Column(db.VARCHAR(40), unique=True)
    artif_depository = db.Column(db.VARCHAR(40))
    depository_id = db.Column(db.VARCHAR(40), unique=True)
    description =  db.Column(db.Text)
    stamp_location_description = db.Column(db.Text)
    artif_g = db.Column(db.VARCHAR(15))
    artif_preservation = db.Column(db.VARCHAR(15))
    munsell_hue = db.Column(db.VARCHAR(7))
    munsell_value = db.Column(db.VARCHAR(20))
    munsell_chroma = db.Column(db.VARCHAR(20))
    munsell_code = db.Column(db.VARCHAR (20))
    munsell_name = db.Column(db.VARCHAR (30))
    xlink300px_artif = db.Column(db.VARCHAR(80))
    xlink1000px_artif = db.Column(db.VARCHAR(80))
    zlink300px_artif = db.Column(db.VARCHAR(80))
    zlink1000px_artif = db.Column(db.VARCHAR(80))
    # Определение модели Artifact
     # // year_exc, artif_position(location), artif_g(groups), munsell_name

class Stamp(db.Model):
    __tablename__ = 'stamp'
    id = db.Column(db.CHAR(6), primary_key=True)
    artifact_id = db.Column(db.SmallInteger, db.ForeignKey('artifact.id'))
    stamp_position = db.Column(db.VARCHAR(12))
    stamp_preservation = db.Column(db.VARCHAR(12))
    stamp_preservation_comm = db.Column(db.VARCHAR(40))
    relief_type = db.Column(db.VARCHAR(20))
    content_type = db.Column(db.VARCHAR(20))
    shape_type = db.Column(db.VARCHAR(40))
    axis_large = db.Column(db.SmallInteger)
    axis_small = db.Column(db.SmallInteger)
    origin_type = db.Column(db.VARCHAR(15))
    magist_name = db.Column(db.VARCHAR(30))
    fabric_name = db.Column(db.VARCHAR(30))
    stamp_legend = db.Column(db.Text)
    stamp_legend_comment = db.Column(db.VARCHAR(500))
    emblem = db.Column(db.VARCHAR(200))
    date_text = db.Column(db.VARCHAR(50))
    date_early = db.Column(db.SmallInteger)
    date_late = db.Column(db.SmallInteger)
    finkelstein = db.Column(db.VARCHAR(20))
    garlan = db.Column(db.VARCHAR(20))
    stamp_comments = db.Column(db.Text)
    published = db.Column(db.VARCHAR(100))

    xlink300px = db.Column(db.VARCHAR(150))
    xlink1000px = db.Column(db.VARCHAR(150))

    zlink300px = db.Column(db.VARCHAR(150))
    zlink1000px = db.Column(db.VARCHAR(150))

    glink300px = db.Column(db.VARCHAR(150))
    glink1000px = db.Column(db.VARCHAR(150))

    g2link300px = db.Column(db.VARCHAR(150))
    g2link1000px = db.Column(db.VARCHAR(150))

    g3link300px = db.Column(db.VARCHAR(150))
    g3link1000px = db.Column(db.VARCHAR(150))

    g4link300px = db.Column(db.VARCHAR(150))
    g4link1000px = db.Column(db.VARCHAR(150))

    g5link300px = db.Column(db.VARCHAR(150))
    g5link1000px = db.Column(db.VARCHAR(150))

    g6link300px = db.Column(db.VARCHAR(150))
    g6link1000px = db.Column(db.VARCHAR(150))


class Model_3d(db.Model):
    __tablename__ = 'model_3d'
    model_id = db.Column(db.SmallInteger, primary_key=True)
    stamp_id = db.Column(db.SmallInteger, db.ForeignKey('stamp.id'))
    polygon_count = db.Column(db.Integer)
    polygon_sm = db.Column(db.Integer)
    polygon_size = db.Column(db.Integer)
    model_process = db.Column(db.VARCHAR(30))
    frame_count = db.Column(db.Integer)
    camera = db.Column(db.VARCHAR(40))
    lens = db.Column(db.VARCHAR(40))
    model_date = db.Column(db.Date)
    model_link = db.Column(db.VARCHAR(50))


class Мodel_3d_artif(db.Model):
    __tablename__ = 'model_3d_artifact'
    model_id_artif = db.Column(db.SmallInteger, primary_key=True)
    artifact_id = db.Column(db.SmallInteger, db.ForeignKey('artifact.id'))
    polygon_count_artif = db.Column(db.Integer)
    polygon_sm_artif = db.Column(db.Integer)
    polygon_size_artif = db.Column(db.Integer)
    model_process_artif = db.Column(db.VARCHAR(30))
    frame_count_artif = db.Column(db.Integer)
    camera_artif = db.Column(db.VARCHAR(40))
    lens_artif = db.Column(db.VARCHAR(40))
    model_date_artif = db.Column(db.Date)
    model_link_artif = db.Column(db.VARCHAR(50))


    # class Image(db.Model):
#     __tablename__ = 'image'
#     image_id = db.Column(db.SmallInteger, primary_key=True)
#     stamp_id = db.Column(db.SmallInteger, db.ForeignKey('stamp.id'))
#     image_type = db.Column(db.VARCHAR(40))
#     image_description = db.Column(db.Text ())
#     link300px = db.Column(db.VARCHAR(80))
#     link1000px = db.Column(db.VARCHAR(80))
import os
import sys
from flask import Flask, jsonify, request, send_from_directory
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, CORS_ORIGINS
from models import db, Site, Manufact, Artifact, Stamp, Model_3d, Мodel_3d_artif
from schemas import site_schema, sites_schema, manufact_schema, manufacts_schema, artifact_schema, artifacts_schema, stamp_schema, stamps_schema, model_3d_schema, models_3d_schema, model_3d_artif_schema, models_3d_artif_schema

from configdb import encoded_username, encoded_password

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": CORS_ORIGINS}})

app = Flask(__name__, static_folder='/home/u187324/amphorastamps.rssda.su/www/static/')
CORS(app, resources={r"/*": {"origins": "https://amphorastamps.rssda.su"}})

# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{encoded_username}:{encoded_password}@185.84.108.3/b187324_stamps'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
ma = Marshmallow(app)
# Инициализация базы данных
db.init_app(app)

@app.route('/get_years', methods=['GET'])
def get_years():
    years = Artifact.query.with_entities(Artifact.year_exc.distinct()).all()
    year_list = [year[0] for year in years if year[0] is not None]
    return jsonify(year_list)

@app.route('/get_locations', methods=['GET'])
def get_locations():
    locations = Artifact.query.with_entities(Artifact.artif_position.distinct()).all()
    location_list = [location[0] for location in locations if location[0] is not None]
    return jsonify(location_list)

@app.route('/get_groups', methods=['GET'])
def get_groups():
    groups = Artifact.query.with_entities(Artifact.artif_g.distinct()).all()
    group_list = [group[0] for group in groups if group[0] is not None]
    return jsonify(group_list)

@app.route('/get_colors', methods=['GET'])
def get_colors():
    colors = Artifact.query.with_entities(Artifact.munsell_name.distinct()).all()
    color_list = [color[0] for color in colors if color[0] is not None]
    return jsonify(color_list)
    # // stamp_position, stamp_preservation, relief_type, content_type, shape_type, origin_type
@app.route('/get_positions', methods=['GET'])
def get_positions():
    positions = Stamp.query.with_entities(Stamp.stamp_position.distinct()).all()
    position_list = [position[0] for position in positions if position[0] is not None]
    return jsonify(position_list)

@app.route('/get_preservations', methods=['GET'])
def get_preservations():
    preservations = Stamp.query.with_entities(Stamp.stamp_preservation.distinct()).all()
    preservation_list = [preservation[0] for preservation in preservations if preservation[0] is not None]
    return jsonify(preservation_list)

@app.route('/get_reliefs', methods=['GET'])
def get_reliefs():
    reliefs = Stamp.query.with_entities(Stamp.relief_type.distinct()).all()
    relief_list = [relief[0] for relief in reliefs if relief[0] is not None]
    return jsonify(relief_list)

@app.route('/get_contents', methods=['GET'])
def get_contents():
    contents = Stamp.query.with_entities(Stamp.content_type.distinct()).all()
    content_list = [content[0] for content in contents if content[0] is not None]
    return jsonify(content_list)

@app.route('/get_shapes', methods=['GET'])
def get_shapes():
    shapes = Stamp.query.with_entities(Stamp.shape_type.distinct()).all()
    shape_list = [shape[0] for shape in shapes if shape[0] is not None]
    return jsonify(shape_list)

@app.route('/get_origins', methods=['GET'])
def get_origins():
    origins = Stamp.query.with_entities(Stamp.origin_type.distinct()).all()
    origin_list = [origin[0] for origin in origins if origin[0] is not None]
    return jsonify(origin_list)
# // date_early, date_late, finkelstein, garlan, emblem??? axis_small??, axis_large??
@app.route('/get_earlys', methods=['GET'])
def get_earlys():
    earlys = Stamp.query.with_entities(Stamp.date_early.distinct()).all()
    early_list = [early[0] for early in earlys if early[0] is not None]
    return jsonify(early_list)

@app.route('/get_lates', methods=['GET'])
def get_lates():
    lates = Stamp.query.with_entities(Stamp.date_late.distinct()).all()
    late_list = [late[0] for late in lates if late[0] is not None]
    return jsonify(late_list)

@app.route('/get_fis', methods=['GET'])
def get_fis():
    fis = Stamp.query.with_entities(Stamp.finkelstein.distinct()).all()
    fi_list = [fi[0] for fi in fis if fi[0] is not None]
    return jsonify(fi_list)

@app.route('/get_garlans', methods=['GET'])
def get_finkelsteins():
    garlans = Stamp.query.with_entities(Stamp.garlan.distinct()).all()
    garlan_list = [garlan[0] for garlan in garlans if garlan[0] is not None]
    return jsonify(garlan_list)

@app.route('/get_magists', methods=['GET'])
def get_magists():
    magists = Stamp.query.with_entities(Stamp.magist_name.distinct()).all()
    magist_list = [magist[0] for magist in magists if magist[0] is not None]
    return jsonify(magist_list)

@app.route('/get_fabrics', methods=['GET'])
def get_fabrics():
    fabrics = Stamp.query.with_entities(Stamp.fabric_name.distinct()).all()
    fabric_list = [fabric[0] for fabric in fabrics if fabric[0] is not None]
    return jsonify(fabric_list)

@app.route('/get_emblems', methods=['GET'])
def get_emblems():
    emblems = Stamp.query.with_entities(Stamp.emblem.distinct()).all()
    emblem_list = [emblem[0] for emblem in emblems if emblem[0] is not None]
    return jsonify(emblem_list)




@app.route('/get_all', methods=['GET'])
def get_all():
    query = db.session.query(Site, Manufact, Artifact, Stamp, Model_3d).\
            filter(Site.id == Artifact.site_id).\
            filter(Manufact.id == Artifact.manufact_id).\
            filter(Artifact.id == Stamp.artifact_id).\
            filter(Stamp.id == Model_3d.stamp_id)

    params = {
        'site_id': Site.id,
        'manufact_id': Manufact.id,
        'stamp_legend': Stamp.stamp_legend.ilike,
        'year_exc': Artifact.year_exc,
        'artif_position': Artifact.artif_position,
        'artif_g': Artifact.artif_g,
        'munsell_name': Artifact.munsell_name,
        'stamp_position': Stamp.stamp_position,
        'stamp_preservation': Stamp.stamp_preservation,
        'relief_type': Stamp.relief_type,
        'content_type': Stamp.content_type,
        'shape_type': Stamp.shape_type,
        'origin_type': Stamp.origin_type,
        'date_early': Stamp.date_early,
        'date_late': Stamp.date_late,
        'finkelstein': Stamp.finkelstein,
        'garlan': Stamp.garlan,
        'fabric_name': Stamp.fabric_name,
        'magist_name': Stamp.magist_name,
        'emblem': Stamp.emblem,
        'stamp_comments': Stamp.stamp_comments,
        'published':Stamp.published
    }

    for param, column in params.items():
        value = request.args.get(param)
        if value is not None:
            if param == 'stamp_legend':
                query = query.filter(column(f"%{value}%"))
            else:
                query = query.filter(column == value)

    joined_tables = query.all()

    results = []

    for site, manufact, artifact, stamp, model_3d in joined_tables:
        site_data = site_schema.dump(site)
        manufact_data = manufact_schema.dump(manufact)
        artifact_data = artifact_schema.dump(artifact)
        stamp_data = stamp_schema.dump(stamp)
        model_3d_data = model_3d_schema.dump(model_3d)

        data = {**site_data, **manufact_data, **artifact_data, **stamp_data, **model_3d_data}
        results.append(data)

    return jsonify(results)


@app.route('/get_item/<int:id>', methods=['GET'])
def get_item(id):
    joined_tables = db.session.query(Site, Manufact, Artifact, Stamp, Model_3d).filter(
        Site.id == Artifact.site_id,
        Manufact.id == Artifact.manufact_id,
        Artifact.id == Stamp.artifact_id,
        Stamp.id == Model_3d.stamp_id,
        Stamp.id == id  # filter by id
    ).all()

    if not joined_tables:
        return jsonify({'message': 'Item not found'}), 404
    
    site, manufact, artifact, stamp, model_3d = joined_tables[0]

    site_data = site_schema.dump(site)
    manufact_data = manufact_schema.dump(manufact)
    artifact_data = artifact_schema.dump(artifact)
    stamp_data = stamp_schema.dump(stamp)
    model_3d_data = model_3d_schema.dump(model_3d)

    data = {**site_data, **manufact_data, **artifact_data, **stamp_data, **model_3d_data}

    return jsonify(data)


@app.route('/get_sites', methods = ['GET'])
def get_sites():
    all_sites = Site.query.all()
    results = sites_schema.dump(all_sites)
    return jsonify(results)

@app.route('/get_sites/<id>/', methods = ['GET'])
def get_ditailes_site(id):
    site = Site.query.get(id)
    return site_schema.jsonify(site)



@app.route('/get_manufacts', methods = ['GET'])
def get_manufacts():
    all_manufacts = Manufact.query.all()
    results = manufacts_schema.dump(all_manufacts)
    return jsonify(results)

@app.route('/get_manufacts/<id>/', methods = ['GET'])
def get_ditailes_manufact(id):
    manufact = Manufact.query.get(id)
    return manufact_schema.jsonify(manufact)

@app.route('/get_models', methods = ['GET'])
def get_models():
    all_models = Model_3d.query.all()
    results = models_3d_schema.dump(all_models)
    return jsonify(results)

@app.route('/get_model/<model_id>/', methods = ['GET'])
def get_model(model_id):
    model = Model_3d.query.get(model_id)
    return model_3d_schema.jsonify(model)

# if __name__== "__main__":
#     app.run(debug=True, host="0.0.0.0", port=8000)

@app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')
    
if __name__== "__main__":
    app.run()
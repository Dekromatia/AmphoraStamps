from flask_marshmallow import Marshmallow

ma = Marshmallow()

class SiteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'site_name', 'site_latitude', 'site_longitude')

site_schema = SiteSchema()
sites_schema = SiteSchema(many=True)


class ManufactSchema(ma.Schema):
    class Meta:
        fields = ('id', 'manufact_center', 'manufact_latitude', 'manufact_longitude')

manufact_schema = ManufactSchema()
manufacts_schema = ManufactSchema(many=True)

class ArtifactSchema(ma.Schema):
    class Meta:
        fields = ('id', 'site_id', 'manufact_id', 'year_exc', 'unit_exc', 'leader_exc', 'artif_position', 'field_id',
                  'artif_depository', 'depository_id', 'description', 'stamp_location_description', 'artif_g', 'artif_preservation', 'munsell_hue', 
                  'munsell_value', 'munsell_chroma', 'munsell_code', 'munsell_name', 
                  'xlink300px_artif', 'xlink1000px_artif', 'zlink300px_artif','zlink1000px_artif',
                  )

artifact_schema = ArtifactSchema()
artifacts_schema = ArtifactSchema(many=True)



class StampSchema(ma.Schema):
    class Meta:
        fields = ('date_early', 'date_late', 'axis_large', 'axis_small', 'artifact_id', 'id', 'shape_type',
                   'origin_type', 'magist_name', 'fabric_name', 'stamp_legend', 'stamp_legend_comment',
                     'emblem', 'date_text', 'finkelstein', 'garlan', 'stamp_comments', 'stamp_position',
                       'stamp_preservation', 'stamp_preservation_comm',
                        'xlink300px', 'xlink1000px', 'zlink300px','zlink1000px',
                        'glink300px', 'glink1000px', 'g2link300px', 'g2link1000px', 'g3link300px', 'g3link1000px',
                        'g4link300px', 'g4link1000px', 'g5link300px', 'g5link1000px', 'g6link300px', 'g6link1000px', 
                        'relief_type', 'content_type', 'published')

stamp_schema = StampSchema()
stamps_schema = StampSchema(many=True)


class Model_3dSchema(ma.Schema):
    class Meta:
        fields = ('model_id', 'stamp_id', 'polygon_count', 'polygon_sm', 'polygon_size', 'model_process',
                  'frame_count', 'camera', 'lens', 'model_date', 'model_link')

model_3d_schema = Model_3dSchema()
models_3d_schema = Model_3dSchema(many=True)


class Мodel_3d_artifSchema(ma.Schema):
    class Meta:
        fields = ('model_id_artif', 'artifact_id', 'polygon_count_artif', 'polygon_sm_artif', 'polygon_size_artif',
                   'model_process_artif', 'frame_count_artif', 'camera_artif', 'lens_artif', 'model_date_artif', 'model_link_artif')

model_3d_artif_schema = Мodel_3d_artifSchema()
models_3d_artif_schema = Мodel_3d_artifSchema(many=True)


# class ImageSchema(ma.Schema):
#     class Meta:
#         fields = ('image_id', 'stamp_id', 'image_type', 'image_description', 'link300px', 'link1000px')

# image_schema = ImageSchema()
# images_schema = ImageSchema(many=True)
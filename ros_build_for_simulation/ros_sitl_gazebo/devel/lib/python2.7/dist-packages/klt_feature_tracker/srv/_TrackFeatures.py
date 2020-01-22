# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from klt_feature_tracker/TrackFeaturesRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg
import sensor_msgs.msg

class TrackFeaturesRequest(genpy.Message):
  _md5sum = "e6ba594a5fc048bf5a4498bc48e6665e"
  _type = "klt_feature_tracker/TrackFeaturesRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """sensor_msgs/Image left_image
sensor_msgs/Image right_image
int32[] update_vect
int32 stereo

================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  __slots__ = ['left_image','right_image','update_vect','stereo']
  _slot_types = ['sensor_msgs/Image','sensor_msgs/Image','int32[]','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       left_image,right_image,update_vect,stereo

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TrackFeaturesRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.left_image is None:
        self.left_image = sensor_msgs.msg.Image()
      if self.right_image is None:
        self.right_image = sensor_msgs.msg.Image()
      if self.update_vect is None:
        self.update_vect = []
      if self.stereo is None:
        self.stereo = 0
    else:
      self.left_image = sensor_msgs.msg.Image()
      self.right_image = sensor_msgs.msg.Image()
      self.update_vect = []
      self.stereo = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.left_image.header.seq, _x.left_image.header.stamp.secs, _x.left_image.header.stamp.nsecs))
      _x = self.left_image.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.left_image.height, _x.left_image.width))
      _x = self.left_image.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.left_image.is_bigendian, _x.left_image.step))
      _x = self.left_image.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.right_image.header.seq, _x.right_image.header.stamp.secs, _x.right_image.header.stamp.nsecs))
      _x = self.right_image.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.right_image.height, _x.right_image.width))
      _x = self.right_image.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.right_image.is_bigendian, _x.right_image.step))
      _x = self.right_image.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.update_vect)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.update_vect))
      buff.write(_get_struct_i().pack(self.stereo))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.left_image is None:
        self.left_image = sensor_msgs.msg.Image()
      if self.right_image is None:
        self.right_image = sensor_msgs.msg.Image()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.left_image.header.seq, _x.left_image.header.stamp.secs, _x.left_image.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.left_image.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.left_image.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.left_image.height, _x.left_image.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.left_image.encoding = str[start:end].decode('utf-8')
      else:
        self.left_image.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.left_image.is_bigendian, _x.left_image.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.left_image.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.right_image.header.seq, _x.right_image.header.stamp.secs, _x.right_image.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.right_image.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.right_image.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.right_image.height, _x.right_image.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.right_image.encoding = str[start:end].decode('utf-8')
      else:
        self.right_image.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.right_image.is_bigendian, _x.right_image.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.right_image.data = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.update_vect = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (self.stereo,) = _get_struct_i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.left_image.header.seq, _x.left_image.header.stamp.secs, _x.left_image.header.stamp.nsecs))
      _x = self.left_image.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.left_image.height, _x.left_image.width))
      _x = self.left_image.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.left_image.is_bigendian, _x.left_image.step))
      _x = self.left_image.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.right_image.header.seq, _x.right_image.header.stamp.secs, _x.right_image.header.stamp.nsecs))
      _x = self.right_image.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.right_image.height, _x.right_image.width))
      _x = self.right_image.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.right_image.is_bigendian, _x.right_image.step))
      _x = self.right_image.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.update_vect)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.update_vect.tostring())
      buff.write(_get_struct_i().pack(self.stereo))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.left_image is None:
        self.left_image = sensor_msgs.msg.Image()
      if self.right_image is None:
        self.right_image = sensor_msgs.msg.Image()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.left_image.header.seq, _x.left_image.header.stamp.secs, _x.left_image.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.left_image.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.left_image.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.left_image.height, _x.left_image.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.left_image.encoding = str[start:end].decode('utf-8')
      else:
        self.left_image.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.left_image.is_bigendian, _x.left_image.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.left_image.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.right_image.header.seq, _x.right_image.header.stamp.secs, _x.right_image.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.right_image.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.right_image.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.right_image.height, _x.right_image.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.right_image.encoding = str[start:end].decode('utf-8')
      else:
        self.right_image.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.right_image.is_bigendian, _x.right_image.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.right_image.data = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.update_vect = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (self.stereo,) = _get_struct_i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_BI = None
def _get_struct_BI():
    global _struct_BI
    if _struct_BI is None:
        _struct_BI = struct.Struct("<BI")
    return _struct_BI
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from klt_feature_tracker/TrackFeaturesResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class TrackFeaturesResponse(genpy.Message):
  _md5sum = "b2c0cf55e2ad9e563c111a72cc01130a"
  _type = "klt_feature_tracker/TrackFeaturesResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32[] update_vect
float64[] features_l
float64[] features_r

"""
  __slots__ = ['update_vect','features_l','features_r']
  _slot_types = ['int32[]','float64[]','float64[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       update_vect,features_l,features_r

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TrackFeaturesResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.update_vect is None:
        self.update_vect = []
      if self.features_l is None:
        self.features_l = []
      if self.features_r is None:
        self.features_r = []
    else:
      self.update_vect = []
      self.features_l = []
      self.features_r = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.update_vect)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.update_vect))
      length = len(self.features_l)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.features_l))
      length = len(self.features_r)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.features_r))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.update_vect = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.features_l = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.features_r = struct.unpack(pattern, str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.update_vect)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.update_vect.tostring())
      length = len(self.features_l)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.features_l.tostring())
      length = len(self.features_r)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.features_r.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.update_vect = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.features_l = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.features_r = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
class TrackFeatures(object):
  _type          = 'klt_feature_tracker/TrackFeatures'
  _md5sum = 'd55c173a9d514c7ff49f3816cbda7316'
  _request_class  = TrackFeaturesRequest
  _response_class = TrackFeaturesResponse

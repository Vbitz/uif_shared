# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uif.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tuif.proto\x12\x03uif\"\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"@\n\tRectangle\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02\"\x1b\n\nSolidBrush\x12\r\n\x05\x63olor\x18\x01 \x01(\r\"/\n\x0cGradientStop\x12\r\n\x05\x63olor\x18\x01 \x01(\r\x12\x10\n\x08position\x18\x02 \x01(\x02\"k\n\x13LinearGradientBrush\x12 \n\x05stops\x18\x01 \x03(\x0b\x32\x11.uif.GradientStop\x12\x19\n\x05start\x18\x02 \x01(\x0b\x32\n.uif.Point\x12\x17\n\x03\x65nd\x18\x03 \x01(\x0b\x32\n.uif.Point\"]\n\x05\x42rush\x12 \n\x05solid\x18\x01 \x01(\x0b\x32\x0f.uif.SolidBrushH\x00\x12*\n\x06linear\x18\x02 \x01(\x0b\x32\x18.uif.LinearGradientBrushH\x00\x42\x06\n\x04kind\"\x8d\x01\n\rRectangleNode\x12\x1c\n\x04rect\x18\x01 \x01(\x0b\x32\x0e.uif.Rectangle\x12\x1a\n\x06stroke\x18\x02 \x01(\x0b\x32\n.uif.Brush\x12\x0e\n\x06\x66illed\x18\x03 \x01(\x08\x12\x18\n\x10rounded_radius_x\x18\x04 \x01(\x02\x12\x18\n\x10rounded_radius_y\x18\x05 \x01(\x02\"\x8a\x02\n\x0cTextEditSpan\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\x0e\n\x06length\x18\x02 \x01(\x05\x12\x13\n\tfont_name\x18\x04 \x01(\tH\x00\x12&\n\x0b\x66ont_weight\x18\x05 \x01(\x0e\x32\x0f.uif.FontWeightH\x00\x12$\n\nfont_style\x18\x06 \x01(\x0e\x32\x0e.uif.FontStyleH\x00\x12(\n\x0c\x66ont_stretch\x18\x07 \x01(\x0e\x32\x10.uif.FontStretchH\x00\x12\x13\n\tfont_size\x18\x08 \x01(\x02H\x00\x12\x1b\n\x05\x62rush\x18\t \x01(\x0b\x32\n.uif.BrushH\x00\x12\x13\n\tunderline\x18\n \x01(\x08H\x00\x42\x06\n\x04\x65\x64it\"\xe5\x02\n\x08TextNode\x12\x1e\n\x06\x62ounds\x18\x01 \x01(\x0b\x32\x0e.uif.Rectangle\x12\x1a\n\x06stroke\x18\x02 \x01(\x0b\x32\n.uif.Brush\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x11\n\tfont_name\x18\x04 \x01(\t\x12$\n\x0b\x66ont_weight\x18\x05 \x01(\x0e\x32\x0f.uif.FontWeight\x12\"\n\nfont_style\x18\x06 \x01(\x0e\x32\x0e.uif.FontStyle\x12&\n\x0c\x66ont_stretch\x18\x07 \x01(\x0e\x32\x10.uif.FontStretch\x12\x11\n\tfont_size\x18\x08 \x01(\x02\x12\"\n\ntext_align\x18\t \x01(\x0e\x32\x0e.uif.TextAlign\x12,\n\x0fparagraph_align\x18\n \x01(\x0e\x32\x13.uif.ParagraphAlign\x12%\n\nedit_spans\x18\x0b \x03(\x0b\x32\x11.uif.TextEditSpan\"A\n\x07PCBegin\x12\x1e\n\x04kind\x18\x01 \x01(\x0e\x32\x10.uif.PCBeginKind\x12\x16\n\x02pt\x18\x02 \x01(\x0b\x32\n.uif.Point\"%\n\x05PCEnd\x12\x1c\n\x04kind\x18\x01 \x01(\x0e\x32\x0e.uif.PCEndKind\"\"\n\x08PCLineTo\x12\x16\n\x02pt\x18\x01 \x01(\x0b\x32\n.uif.Point\"c\n\x0cPCCubicCurve\x12\x1c\n\x08\x63ontrol1\x18\x01 \x01(\x0b\x32\n.uif.Point\x12\x1c\n\x08\x63ontrol2\x18\x02 \x01(\x0b\x32\n.uif.Point\x12\x17\n\x03\x65nd\x18\x03 \x01(\x0b\x32\n.uif.Point\"I\n\x10PCQuadraticCurve\x12\x1c\n\x08\x63ontrol1\x18\x01 \x01(\x0b\x32\n.uif.Point\x12\x17\n\x03\x65nd\x18\x02 \x01(\x0b\x32\n.uif.Point\"\x89\x01\n\x05PCArc\x12\x10\n\x08x_radius\x18\x01 \x01(\x02\x12\x10\n\x08y_radius\x18\x02 \x01(\x02\x12\x17\n\x0fx_axis_rotation\x18\x03 \x01(\x02\x12\x16\n\x0elarge_arc_flag\x18\x04 \x01(\x08\x12\x12\n\nsweep_flag\x18\x05 \x01(\x08\x12\x17\n\x03\x65nd\x18\x06 \x01(\x0b\x32\n.uif.Point\"\xdf\x01\n\x0bPathCommand\x12\x1d\n\x05\x62\x65gin\x18\n \x01(\x0b\x32\x0c.uif.PCBeginH\x00\x12\x19\n\x03\x65nd\x18\x14 \x01(\x0b\x32\n.uif.PCEndH\x00\x12 \n\x07line_to\x18\x0b \x01(\x0b\x32\r.uif.PCLineToH\x00\x12%\n\x08\x63ubic_to\x18\x0c \x01(\x0b\x32\x11.uif.PCCubicCurveH\x00\x12(\n\x07quad_to\x18\r \x01(\x0b\x32\x15.uif.PCQuadraticCurveH\x00\x12\x1c\n\x06\x61rc_to\x18\x0e \x01(\x0b\x32\n.uif.PCArcH\x00\x42\x05\n\x03\x63md\"]\n\x08PathNode\x12\"\n\x08\x63ommands\x18\x01 \x03(\x0b\x32\x10.uif.PathCommand\x12\x11\n\tis_filled\x18\x02 \x01(\x08\x12\x1a\n\x06stroke\x18\x03 \x01(\x0b\x32\n.uif.Brush\"\x0b\n\tEmptyNode\",\n\x0c\x43lipRectNode\x12\x1c\n\x04rect\x18\x01 \x01(\x0b\x32\x0e.uif.Rectangle\"\x87\x03\n\x0b\x45\x64itCommand\x12\x11\n\ttimestamp\x18\x05 \x01(\x04\x12\x11\n\tclient_id\x18\x04 \x01(\t\x12\'\n\x04kind\x18\x01 \x01(\x0e\x32\x19.uif.EditCommand.EditKind\x12\x11\n\tparent_id\x18\x02 \x01(\x04\x12\x11\n\tobject_id\x18\x03 \x01(\x04\x12\"\n\x04rect\x18\n \x01(\x0b\x32\x12.uif.RectangleNodeH\x00\x12\x1d\n\x04text\x18\x0b \x01(\x0b\x32\r.uif.TextNodeH\x00\x12\x1d\n\x04path\x18\x0c \x01(\x0b\x32\r.uif.PathNodeH\x00\x12\x1f\n\x05\x65mpty\x18\x14 \x01(\x0b\x32\x0e.uif.EmptyNodeH\x00\x12!\n\x04\x63lip\x18\x15 \x01(\x0b\x32\x11.uif.ClipRectNodeH\x00\"U\n\x08\x45\x64itKind\x12\x10\n\x0c\x41PPEND_CHILD\x10\x00\x12\x10\n\x0cREPLACE_NODE\x10\x01\x12\x12\n\x0e\x43LEANUP_CLIENT\x10\x02\x12\x11\n\rDELETE_OBJECT\x10\x03\x42\x06\n\x04node\"-\n\x07\x45\x64itReq\x12\"\n\x08\x63ommands\x18\x02 \x03(\x0b\x32\x10.uif.EditCommand\"\n\n\x08\x45\x64itResp\"!\n\x0cGetEventsReq\x12\x11\n\tclient_id\x18\x01 \x01(\t\"\x1c\n\nCloseEvent\x12\x0e\n\x06\x63losed\x18\x01 \x01(\x08\"l\n\nMouseEvent\x12 \n\x06\x62utton\x18\x01 \x01(\x0e\x32\x10.uif.MouseButton\x12\x1e\n\x05state\x18\x02 \x01(\x0e\x32\x0f.uif.MouseState\x12\x1c\n\x08location\x18\x03 \x01(\x0b\x32\n.uif.Point\"?\n\rKeyboardEvent\x12\x1c\n\x05state\x18\x01 \x01(\x0e\x32\r.uif.KeyState\x12\x10\n\x08key_code\x18\x02 \x01(\r\"a\n\x0cTextHitEvent\x12\x1e\n\x05mouse\x18\x01 \x01(\x0b\x32\x0f.uif.MouseEvent\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12\x0e\n\x06length\x18\x03 \x01(\r\x12\x11\n\tobject_id\x18\x04 \x01(\x04\"\x9d\x01\n\x05\x45vent\x12 \n\x05\x63lose\x18\n \x01(\x0b\x32\x0f.uif.CloseEventH\x00\x12 \n\x05mouse\x18\x0b \x01(\x0b\x32\x0f.uif.MouseEventH\x00\x12!\n\x03key\x18\x0c \x01(\x0b\x32\x12.uif.KeyboardEventH\x00\x12$\n\x07textHit\x18\r \x01(\x0b\x32\x11.uif.TextHitEventH\x00\x42\x07\n\x05\x65vent\"\x18\n\x16GetServerPropertiesReq\"F\n\x17GetServerPropertiesResp\x12\x14\n\x0cwindow_width\x18\x01 \x01(\r\x12\x15\n\rwindow_height\x18\x02 \x01(\r\"!\n\x10SetClearColorReq\x12\r\n\x05\x63olor\x18\x01 \x01(\r\"\x13\n\x11SetClearColorResp*Q\n\tFontStyle\x12\x15\n\x11\x46ONT_STYLE_NORMAL\x10\x00\x12\x16\n\x12\x46ONT_STYLE_OBLIQUE\x10\x01\x12\x15\n\x11\x46ONT_STYLE_ITALIC\x10\x02*\xc8\x02\n\nFontWeight\x12\x19\n\x15\x46ONT_WEIGHT_UNDEFINED\x10\x00\x12\x14\n\x10\x46ONT_WEIGHT_THIN\x10\x64\x12\x1c\n\x17\x46ONT_WEIGHT_EXTRA_LIGHT\x10\xc8\x01\x12\x16\n\x11\x46ONT_WEIGHT_LIGHT\x10\xac\x02\x12\x1b\n\x16\x46ONT_WEIGHT_SEMI_LIGHT\x10\xde\x02\x12\x17\n\x12\x46ONT_WEIGHT_NORMAL\x10\x90\x03\x12\x17\n\x12\x46ONT_WEIGHT_MEDIUM\x10\xf4\x03\x12\x1a\n\x15\x46ONT_WEIGHT_SEMI_BOLD\x10\xd8\x04\x12\x15\n\x10\x46ONT_WEIGHT_BOLD\x10\xbc\x05\x12\x1b\n\x16\x46ONT_WEIGHT_EXTRA_BOLD\x10\xa0\x06\x12\x16\n\x11\x46ONT_WEIGHT_BLACK\x10\x84\x07\x12\x1c\n\x17\x46ONT_WEIGHT_EXTRA_BLACK\x10\xb6\x07*\xc0\x02\n\x0b\x46ontStretch\x12\x1a\n\x16\x46ONT_STRETCH_UNDEFINED\x10\x00\x12 \n\x1c\x46ONT_STRETCH_ULTRA_CONDENSED\x10\x01\x12 \n\x1c\x46ONT_STRETCH_EXTRA_CONDENSED\x10\x02\x12\x1a\n\x16\x46ONT_STRETCH_CONDENSED\x10\x03\x12\x1f\n\x1b\x46ONT_STRETCH_SEMI_CONDENSED\x10\x04\x12\x17\n\x13\x46ONT_STRETCH_NORMAL\x10\x05\x12\x1e\n\x1a\x46ONT_STRETCH_SEMI_EXPANDED\x10\x06\x12\x19\n\x15\x46ONT_STRETCH_EXPANDED\x10\x07\x12\x1f\n\x1b\x46ONT_STRETCH_EXTRA_EXPANDED\x10\x08\x12\x1f\n\x1b\x46ONT_STRETCH_ULTRA_EXPANDED\x10\t*m\n\tTextAlign\x12\x16\n\x12TEXT_ALIGN_LEADING\x10\x00\x12\x17\n\x13TEXT_ALIGN_TRAILING\x10\x01\x12\x15\n\x11TEXT_ALIGN_CENTER\x10\x02\x12\x18\n\x14TEXT_ALIGN_JUSTIFIED\x10\x03*_\n\x0eParagraphAlign\x12\x18\n\x14PARAGRAPH_ALIGN_NEAR\x10\x00\x12\x17\n\x13PARAGRAPH_ALIGN_FAR\x10\x01\x12\x1a\n\x16PARAGRAPH_ALIGN_CENTER\x10\x02*?\n\x0bPCBeginKind\x12\x17\n\x13PC_BEGINKIND_FILLED\x10\x00\x12\x17\n\x13PC_BEGINKIND_HOLLOW\x10\x01*7\n\tPCEndKind\x12\x13\n\x0fPC_ENDKIND_OPEN\x10\x00\x12\x15\n\x11PC_ENDKIND_CLOSED\x10\x01*\x96\x01\n\x0bMouseButton\x12\x15\n\x11MOUSE_BUTTON_NONE\x10\x00\x12\x15\n\x11MOUSE_BUTTON_LEFT\x10\x01\x12\x17\n\x13MOUSE_BUTTON_MIDDLE\x10\x02\x12\x16\n\x12MOUSE_BUTTON_RIGHT\x10\x03\x12\x13\n\x0fMOUSE_BUTTON_X1\x10\x04\x12\x13\n\x0fMOUSE_BUTTON_X2\x10\x05*L\n\nMouseState\x12\x14\n\x10MOUSE_STATE_NONE\x10\x00\x12\x12\n\x0eMOUSE_STATE_UP\x10\x01\x12\x14\n\x10MOUSE_STATE_DOWN\x10\x02*/\n\x08KeyState\x12\t\n\x05UNSET\x10\x00\x12\x0c\n\x08KEY_DOWN\x10\x01\x12\n\n\x06KEY_UP\x10\x02\x32\xf2\x01\n\x0bUIFramework\x12#\n\x04\x45\x64it\x12\x0c.uif.EditReq\x1a\r.uif.EditResp\x12,\n\tGetEvents\x12\x11.uif.GetEventsReq\x1a\n.uif.Event0\x01\x12P\n\x13GetServerProperties\x12\x1b.uif.GetServerPropertiesReq\x1a\x1c.uif.GetServerPropertiesResp\x12>\n\rSetClearColor\x12\x15.uif.SetClearColorReq\x1a\x16.uif.SetClearColorRespB\x1dZ\x1bgithub.com/Vbitz/uif_sharedb\x06proto3')

_FONTSTYLE = DESCRIPTOR.enum_types_by_name['FontStyle']
FontStyle = enum_type_wrapper.EnumTypeWrapper(_FONTSTYLE)
_FONTWEIGHT = DESCRIPTOR.enum_types_by_name['FontWeight']
FontWeight = enum_type_wrapper.EnumTypeWrapper(_FONTWEIGHT)
_FONTSTRETCH = DESCRIPTOR.enum_types_by_name['FontStretch']
FontStretch = enum_type_wrapper.EnumTypeWrapper(_FONTSTRETCH)
_TEXTALIGN = DESCRIPTOR.enum_types_by_name['TextAlign']
TextAlign = enum_type_wrapper.EnumTypeWrapper(_TEXTALIGN)
_PARAGRAPHALIGN = DESCRIPTOR.enum_types_by_name['ParagraphAlign']
ParagraphAlign = enum_type_wrapper.EnumTypeWrapper(_PARAGRAPHALIGN)
_PCBEGINKIND = DESCRIPTOR.enum_types_by_name['PCBeginKind']
PCBeginKind = enum_type_wrapper.EnumTypeWrapper(_PCBEGINKIND)
_PCENDKIND = DESCRIPTOR.enum_types_by_name['PCEndKind']
PCEndKind = enum_type_wrapper.EnumTypeWrapper(_PCENDKIND)
_MOUSEBUTTON = DESCRIPTOR.enum_types_by_name['MouseButton']
MouseButton = enum_type_wrapper.EnumTypeWrapper(_MOUSEBUTTON)
_MOUSESTATE = DESCRIPTOR.enum_types_by_name['MouseState']
MouseState = enum_type_wrapper.EnumTypeWrapper(_MOUSESTATE)
_KEYSTATE = DESCRIPTOR.enum_types_by_name['KeyState']
KeyState = enum_type_wrapper.EnumTypeWrapper(_KEYSTATE)
FONT_STYLE_NORMAL = 0
FONT_STYLE_OBLIQUE = 1
FONT_STYLE_ITALIC = 2
FONT_WEIGHT_UNDEFINED = 0
FONT_WEIGHT_THIN = 100
FONT_WEIGHT_EXTRA_LIGHT = 200
FONT_WEIGHT_LIGHT = 300
FONT_WEIGHT_SEMI_LIGHT = 350
FONT_WEIGHT_NORMAL = 400
FONT_WEIGHT_MEDIUM = 500
FONT_WEIGHT_SEMI_BOLD = 600
FONT_WEIGHT_BOLD = 700
FONT_WEIGHT_EXTRA_BOLD = 800
FONT_WEIGHT_BLACK = 900
FONT_WEIGHT_EXTRA_BLACK = 950
FONT_STRETCH_UNDEFINED = 0
FONT_STRETCH_ULTRA_CONDENSED = 1
FONT_STRETCH_EXTRA_CONDENSED = 2
FONT_STRETCH_CONDENSED = 3
FONT_STRETCH_SEMI_CONDENSED = 4
FONT_STRETCH_NORMAL = 5
FONT_STRETCH_SEMI_EXPANDED = 6
FONT_STRETCH_EXPANDED = 7
FONT_STRETCH_EXTRA_EXPANDED = 8
FONT_STRETCH_ULTRA_EXPANDED = 9
TEXT_ALIGN_LEADING = 0
TEXT_ALIGN_TRAILING = 1
TEXT_ALIGN_CENTER = 2
TEXT_ALIGN_JUSTIFIED = 3
PARAGRAPH_ALIGN_NEAR = 0
PARAGRAPH_ALIGN_FAR = 1
PARAGRAPH_ALIGN_CENTER = 2
PC_BEGINKIND_FILLED = 0
PC_BEGINKIND_HOLLOW = 1
PC_ENDKIND_OPEN = 0
PC_ENDKIND_CLOSED = 1
MOUSE_BUTTON_NONE = 0
MOUSE_BUTTON_LEFT = 1
MOUSE_BUTTON_MIDDLE = 2
MOUSE_BUTTON_RIGHT = 3
MOUSE_BUTTON_X1 = 4
MOUSE_BUTTON_X2 = 5
MOUSE_STATE_NONE = 0
MOUSE_STATE_UP = 1
MOUSE_STATE_DOWN = 2
UNSET = 0
KEY_DOWN = 1
KEY_UP = 2


_POINT = DESCRIPTOR.message_types_by_name['Point']
_RECTANGLE = DESCRIPTOR.message_types_by_name['Rectangle']
_SOLIDBRUSH = DESCRIPTOR.message_types_by_name['SolidBrush']
_GRADIENTSTOP = DESCRIPTOR.message_types_by_name['GradientStop']
_LINEARGRADIENTBRUSH = DESCRIPTOR.message_types_by_name['LinearGradientBrush']
_BRUSH = DESCRIPTOR.message_types_by_name['Brush']
_RECTANGLENODE = DESCRIPTOR.message_types_by_name['RectangleNode']
_TEXTEDITSPAN = DESCRIPTOR.message_types_by_name['TextEditSpan']
_TEXTNODE = DESCRIPTOR.message_types_by_name['TextNode']
_PCBEGIN = DESCRIPTOR.message_types_by_name['PCBegin']
_PCEND = DESCRIPTOR.message_types_by_name['PCEnd']
_PCLINETO = DESCRIPTOR.message_types_by_name['PCLineTo']
_PCCUBICCURVE = DESCRIPTOR.message_types_by_name['PCCubicCurve']
_PCQUADRATICCURVE = DESCRIPTOR.message_types_by_name['PCQuadraticCurve']
_PCARC = DESCRIPTOR.message_types_by_name['PCArc']
_PATHCOMMAND = DESCRIPTOR.message_types_by_name['PathCommand']
_PATHNODE = DESCRIPTOR.message_types_by_name['PathNode']
_EMPTYNODE = DESCRIPTOR.message_types_by_name['EmptyNode']
_CLIPRECTNODE = DESCRIPTOR.message_types_by_name['ClipRectNode']
_EDITCOMMAND = DESCRIPTOR.message_types_by_name['EditCommand']
_EDITREQ = DESCRIPTOR.message_types_by_name['EditReq']
_EDITRESP = DESCRIPTOR.message_types_by_name['EditResp']
_GETEVENTSREQ = DESCRIPTOR.message_types_by_name['GetEventsReq']
_CLOSEEVENT = DESCRIPTOR.message_types_by_name['CloseEvent']
_MOUSEEVENT = DESCRIPTOR.message_types_by_name['MouseEvent']
_KEYBOARDEVENT = DESCRIPTOR.message_types_by_name['KeyboardEvent']
_TEXTHITEVENT = DESCRIPTOR.message_types_by_name['TextHitEvent']
_EVENT = DESCRIPTOR.message_types_by_name['Event']
_GETSERVERPROPERTIESREQ = DESCRIPTOR.message_types_by_name['GetServerPropertiesReq']
_GETSERVERPROPERTIESRESP = DESCRIPTOR.message_types_by_name['GetServerPropertiesResp']
_SETCLEARCOLORREQ = DESCRIPTOR.message_types_by_name['SetClearColorReq']
_SETCLEARCOLORRESP = DESCRIPTOR.message_types_by_name['SetClearColorResp']
_EDITCOMMAND_EDITKIND = _EDITCOMMAND.enum_types_by_name['EditKind']
Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.Point)
  })
_sym_db.RegisterMessage(Point)

Rectangle = _reflection.GeneratedProtocolMessageType('Rectangle', (_message.Message,), {
  'DESCRIPTOR' : _RECTANGLE,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.Rectangle)
  })
_sym_db.RegisterMessage(Rectangle)

SolidBrush = _reflection.GeneratedProtocolMessageType('SolidBrush', (_message.Message,), {
  'DESCRIPTOR' : _SOLIDBRUSH,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.SolidBrush)
  })
_sym_db.RegisterMessage(SolidBrush)

GradientStop = _reflection.GeneratedProtocolMessageType('GradientStop', (_message.Message,), {
  'DESCRIPTOR' : _GRADIENTSTOP,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.GradientStop)
  })
_sym_db.RegisterMessage(GradientStop)

LinearGradientBrush = _reflection.GeneratedProtocolMessageType('LinearGradientBrush', (_message.Message,), {
  'DESCRIPTOR' : _LINEARGRADIENTBRUSH,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.LinearGradientBrush)
  })
_sym_db.RegisterMessage(LinearGradientBrush)

Brush = _reflection.GeneratedProtocolMessageType('Brush', (_message.Message,), {
  'DESCRIPTOR' : _BRUSH,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.Brush)
  })
_sym_db.RegisterMessage(Brush)

RectangleNode = _reflection.GeneratedProtocolMessageType('RectangleNode', (_message.Message,), {
  'DESCRIPTOR' : _RECTANGLENODE,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.RectangleNode)
  })
_sym_db.RegisterMessage(RectangleNode)

TextEditSpan = _reflection.GeneratedProtocolMessageType('TextEditSpan', (_message.Message,), {
  'DESCRIPTOR' : _TEXTEDITSPAN,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.TextEditSpan)
  })
_sym_db.RegisterMessage(TextEditSpan)

TextNode = _reflection.GeneratedProtocolMessageType('TextNode', (_message.Message,), {
  'DESCRIPTOR' : _TEXTNODE,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.TextNode)
  })
_sym_db.RegisterMessage(TextNode)

PCBegin = _reflection.GeneratedProtocolMessageType('PCBegin', (_message.Message,), {
  'DESCRIPTOR' : _PCBEGIN,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.PCBegin)
  })
_sym_db.RegisterMessage(PCBegin)

PCEnd = _reflection.GeneratedProtocolMessageType('PCEnd', (_message.Message,), {
  'DESCRIPTOR' : _PCEND,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.PCEnd)
  })
_sym_db.RegisterMessage(PCEnd)

PCLineTo = _reflection.GeneratedProtocolMessageType('PCLineTo', (_message.Message,), {
  'DESCRIPTOR' : _PCLINETO,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.PCLineTo)
  })
_sym_db.RegisterMessage(PCLineTo)

PCCubicCurve = _reflection.GeneratedProtocolMessageType('PCCubicCurve', (_message.Message,), {
  'DESCRIPTOR' : _PCCUBICCURVE,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.PCCubicCurve)
  })
_sym_db.RegisterMessage(PCCubicCurve)

PCQuadraticCurve = _reflection.GeneratedProtocolMessageType('PCQuadraticCurve', (_message.Message,), {
  'DESCRIPTOR' : _PCQUADRATICCURVE,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.PCQuadraticCurve)
  })
_sym_db.RegisterMessage(PCQuadraticCurve)

PCArc = _reflection.GeneratedProtocolMessageType('PCArc', (_message.Message,), {
  'DESCRIPTOR' : _PCARC,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.PCArc)
  })
_sym_db.RegisterMessage(PCArc)

PathCommand = _reflection.GeneratedProtocolMessageType('PathCommand', (_message.Message,), {
  'DESCRIPTOR' : _PATHCOMMAND,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.PathCommand)
  })
_sym_db.RegisterMessage(PathCommand)

PathNode = _reflection.GeneratedProtocolMessageType('PathNode', (_message.Message,), {
  'DESCRIPTOR' : _PATHNODE,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.PathNode)
  })
_sym_db.RegisterMessage(PathNode)

EmptyNode = _reflection.GeneratedProtocolMessageType('EmptyNode', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYNODE,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.EmptyNode)
  })
_sym_db.RegisterMessage(EmptyNode)

ClipRectNode = _reflection.GeneratedProtocolMessageType('ClipRectNode', (_message.Message,), {
  'DESCRIPTOR' : _CLIPRECTNODE,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.ClipRectNode)
  })
_sym_db.RegisterMessage(ClipRectNode)

EditCommand = _reflection.GeneratedProtocolMessageType('EditCommand', (_message.Message,), {
  'DESCRIPTOR' : _EDITCOMMAND,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.EditCommand)
  })
_sym_db.RegisterMessage(EditCommand)

EditReq = _reflection.GeneratedProtocolMessageType('EditReq', (_message.Message,), {
  'DESCRIPTOR' : _EDITREQ,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.EditReq)
  })
_sym_db.RegisterMessage(EditReq)

EditResp = _reflection.GeneratedProtocolMessageType('EditResp', (_message.Message,), {
  'DESCRIPTOR' : _EDITRESP,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.EditResp)
  })
_sym_db.RegisterMessage(EditResp)

GetEventsReq = _reflection.GeneratedProtocolMessageType('GetEventsReq', (_message.Message,), {
  'DESCRIPTOR' : _GETEVENTSREQ,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.GetEventsReq)
  })
_sym_db.RegisterMessage(GetEventsReq)

CloseEvent = _reflection.GeneratedProtocolMessageType('CloseEvent', (_message.Message,), {
  'DESCRIPTOR' : _CLOSEEVENT,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.CloseEvent)
  })
_sym_db.RegisterMessage(CloseEvent)

MouseEvent = _reflection.GeneratedProtocolMessageType('MouseEvent', (_message.Message,), {
  'DESCRIPTOR' : _MOUSEEVENT,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.MouseEvent)
  })
_sym_db.RegisterMessage(MouseEvent)

KeyboardEvent = _reflection.GeneratedProtocolMessageType('KeyboardEvent', (_message.Message,), {
  'DESCRIPTOR' : _KEYBOARDEVENT,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.KeyboardEvent)
  })
_sym_db.RegisterMessage(KeyboardEvent)

TextHitEvent = _reflection.GeneratedProtocolMessageType('TextHitEvent', (_message.Message,), {
  'DESCRIPTOR' : _TEXTHITEVENT,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.TextHitEvent)
  })
_sym_db.RegisterMessage(TextHitEvent)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.Event)
  })
_sym_db.RegisterMessage(Event)

GetServerPropertiesReq = _reflection.GeneratedProtocolMessageType('GetServerPropertiesReq', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVERPROPERTIESREQ,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.GetServerPropertiesReq)
  })
_sym_db.RegisterMessage(GetServerPropertiesReq)

GetServerPropertiesResp = _reflection.GeneratedProtocolMessageType('GetServerPropertiesResp', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVERPROPERTIESRESP,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.GetServerPropertiesResp)
  })
_sym_db.RegisterMessage(GetServerPropertiesResp)

SetClearColorReq = _reflection.GeneratedProtocolMessageType('SetClearColorReq', (_message.Message,), {
  'DESCRIPTOR' : _SETCLEARCOLORREQ,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.SetClearColorReq)
  })
_sym_db.RegisterMessage(SetClearColorReq)

SetClearColorResp = _reflection.GeneratedProtocolMessageType('SetClearColorResp', (_message.Message,), {
  'DESCRIPTOR' : _SETCLEARCOLORRESP,
  '__module__' : 'uif_pb2'
  # @@protoc_insertion_point(class_scope:uif.SetClearColorResp)
  })
_sym_db.RegisterMessage(SetClearColorResp)

_UIFRAMEWORK = DESCRIPTOR.services_by_name['UIFramework']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\033github.com/Vbitz/uif_shared'
  _FONTSTYLE._serialized_start=3114
  _FONTSTYLE._serialized_end=3195
  _FONTWEIGHT._serialized_start=3198
  _FONTWEIGHT._serialized_end=3526
  _FONTSTRETCH._serialized_start=3529
  _FONTSTRETCH._serialized_end=3849
  _TEXTALIGN._serialized_start=3851
  _TEXTALIGN._serialized_end=3960
  _PARAGRAPHALIGN._serialized_start=3962
  _PARAGRAPHALIGN._serialized_end=4057
  _PCBEGINKIND._serialized_start=4059
  _PCBEGINKIND._serialized_end=4122
  _PCENDKIND._serialized_start=4124
  _PCENDKIND._serialized_end=4179
  _MOUSEBUTTON._serialized_start=4182
  _MOUSEBUTTON._serialized_end=4332
  _MOUSESTATE._serialized_start=4334
  _MOUSESTATE._serialized_end=4410
  _KEYSTATE._serialized_start=4412
  _KEYSTATE._serialized_end=4459
  _POINT._serialized_start=18
  _POINT._serialized_end=47
  _RECTANGLE._serialized_start=49
  _RECTANGLE._serialized_end=113
  _SOLIDBRUSH._serialized_start=115
  _SOLIDBRUSH._serialized_end=142
  _GRADIENTSTOP._serialized_start=144
  _GRADIENTSTOP._serialized_end=191
  _LINEARGRADIENTBRUSH._serialized_start=193
  _LINEARGRADIENTBRUSH._serialized_end=300
  _BRUSH._serialized_start=302
  _BRUSH._serialized_end=395
  _RECTANGLENODE._serialized_start=398
  _RECTANGLENODE._serialized_end=539
  _TEXTEDITSPAN._serialized_start=542
  _TEXTEDITSPAN._serialized_end=808
  _TEXTNODE._serialized_start=811
  _TEXTNODE._serialized_end=1168
  _PCBEGIN._serialized_start=1170
  _PCBEGIN._serialized_end=1235
  _PCEND._serialized_start=1237
  _PCEND._serialized_end=1274
  _PCLINETO._serialized_start=1276
  _PCLINETO._serialized_end=1310
  _PCCUBICCURVE._serialized_start=1312
  _PCCUBICCURVE._serialized_end=1411
  _PCQUADRATICCURVE._serialized_start=1413
  _PCQUADRATICCURVE._serialized_end=1486
  _PCARC._serialized_start=1489
  _PCARC._serialized_end=1626
  _PATHCOMMAND._serialized_start=1629
  _PATHCOMMAND._serialized_end=1852
  _PATHNODE._serialized_start=1854
  _PATHNODE._serialized_end=1947
  _EMPTYNODE._serialized_start=1949
  _EMPTYNODE._serialized_end=1960
  _CLIPRECTNODE._serialized_start=1962
  _CLIPRECTNODE._serialized_end=2006
  _EDITCOMMAND._serialized_start=2009
  _EDITCOMMAND._serialized_end=2400
  _EDITCOMMAND_EDITKIND._serialized_start=2307
  _EDITCOMMAND_EDITKIND._serialized_end=2392
  _EDITREQ._serialized_start=2402
  _EDITREQ._serialized_end=2447
  _EDITRESP._serialized_start=2449
  _EDITRESP._serialized_end=2459
  _GETEVENTSREQ._serialized_start=2461
  _GETEVENTSREQ._serialized_end=2494
  _CLOSEEVENT._serialized_start=2496
  _CLOSEEVENT._serialized_end=2524
  _MOUSEEVENT._serialized_start=2526
  _MOUSEEVENT._serialized_end=2634
  _KEYBOARDEVENT._serialized_start=2636
  _KEYBOARDEVENT._serialized_end=2699
  _TEXTHITEVENT._serialized_start=2701
  _TEXTHITEVENT._serialized_end=2798
  _EVENT._serialized_start=2801
  _EVENT._serialized_end=2958
  _GETSERVERPROPERTIESREQ._serialized_start=2960
  _GETSERVERPROPERTIESREQ._serialized_end=2984
  _GETSERVERPROPERTIESRESP._serialized_start=2986
  _GETSERVERPROPERTIESRESP._serialized_end=3056
  _SETCLEARCOLORREQ._serialized_start=3058
  _SETCLEARCOLORREQ._serialized_end=3091
  _SETCLEARCOLORRESP._serialized_start=3093
  _SETCLEARCOLORRESP._serialized_end=3112
  _UIFRAMEWORK._serialized_start=4462
  _UIFRAMEWORK._serialized_end=4704
# @@protoc_insertion_point(module_scope)

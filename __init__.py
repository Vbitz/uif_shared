import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.dirname(__file__), "py"))

import py.uif_pb2 as uif  # noqa: E402
import py.uif_pb2_grpc as uif_grpc  # noqa: E402

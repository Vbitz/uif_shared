$VcpkgPath = "C:\Users\jscar\dev\apps\vcpkg"
$GoBin = "C:\Users\jscar\go\bin"

$Protoc = $VcpkgPath + "\installed\x64-windows\tools\protobuf\protoc.exe"
$GrpcCppPlugin = $VcpkgPath + "\packages\grpc_x64-windows\tools\grpc\grpc_cpp_plugin.exe"

. $Protoc -I. --cpp_out=. .\uif.proto
. $Protoc -I. --grpc_out=. --plugin=protoc-gen-grpc=$GrpcCppPlugin .\uif.proto

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. uif.proto

$Env:PATH += ";" + $GoBin

. $Protoc --go_out=. --go_opt=paths=source_relative --go-grpc_out=. --go-grpc_opt=paths=source_relative uif.proto

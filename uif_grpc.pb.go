// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v3.19.4
// source: uif.proto

package uif_shared

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// UIFrameworkClient is the client API for UIFramework service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type UIFrameworkClient interface {
	Edit(ctx context.Context, in *EditReq, opts ...grpc.CallOption) (*EditResp, error)
	GetEvents(ctx context.Context, in *GetEventsReq, opts ...grpc.CallOption) (UIFramework_GetEventsClient, error)
	GetServerProperties(ctx context.Context, in *GetServerPropertiesReq, opts ...grpc.CallOption) (*GetServerPropertiesResp, error)
	SetClearColor(ctx context.Context, in *SetClearColorReq, opts ...grpc.CallOption) (*SetClearColorResp, error)
}

type uIFrameworkClient struct {
	cc grpc.ClientConnInterface
}

func NewUIFrameworkClient(cc grpc.ClientConnInterface) UIFrameworkClient {
	return &uIFrameworkClient{cc}
}

func (c *uIFrameworkClient) Edit(ctx context.Context, in *EditReq, opts ...grpc.CallOption) (*EditResp, error) {
	out := new(EditResp)
	err := c.cc.Invoke(ctx, "/uif.UIFramework/Edit", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *uIFrameworkClient) GetEvents(ctx context.Context, in *GetEventsReq, opts ...grpc.CallOption) (UIFramework_GetEventsClient, error) {
	stream, err := c.cc.NewStream(ctx, &UIFramework_ServiceDesc.Streams[0], "/uif.UIFramework/GetEvents", opts...)
	if err != nil {
		return nil, err
	}
	x := &uIFrameworkGetEventsClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type UIFramework_GetEventsClient interface {
	Recv() (*Event, error)
	grpc.ClientStream
}

type uIFrameworkGetEventsClient struct {
	grpc.ClientStream
}

func (x *uIFrameworkGetEventsClient) Recv() (*Event, error) {
	m := new(Event)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *uIFrameworkClient) GetServerProperties(ctx context.Context, in *GetServerPropertiesReq, opts ...grpc.CallOption) (*GetServerPropertiesResp, error) {
	out := new(GetServerPropertiesResp)
	err := c.cc.Invoke(ctx, "/uif.UIFramework/GetServerProperties", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *uIFrameworkClient) SetClearColor(ctx context.Context, in *SetClearColorReq, opts ...grpc.CallOption) (*SetClearColorResp, error) {
	out := new(SetClearColorResp)
	err := c.cc.Invoke(ctx, "/uif.UIFramework/SetClearColor", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// UIFrameworkServer is the server API for UIFramework service.
// All implementations must embed UnimplementedUIFrameworkServer
// for forward compatibility
type UIFrameworkServer interface {
	Edit(context.Context, *EditReq) (*EditResp, error)
	GetEvents(*GetEventsReq, UIFramework_GetEventsServer) error
	GetServerProperties(context.Context, *GetServerPropertiesReq) (*GetServerPropertiesResp, error)
	SetClearColor(context.Context, *SetClearColorReq) (*SetClearColorResp, error)
	mustEmbedUnimplementedUIFrameworkServer()
}

// UnimplementedUIFrameworkServer must be embedded to have forward compatible implementations.
type UnimplementedUIFrameworkServer struct {
}

func (UnimplementedUIFrameworkServer) Edit(context.Context, *EditReq) (*EditResp, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Edit not implemented")
}
func (UnimplementedUIFrameworkServer) GetEvents(*GetEventsReq, UIFramework_GetEventsServer) error {
	return status.Errorf(codes.Unimplemented, "method GetEvents not implemented")
}
func (UnimplementedUIFrameworkServer) GetServerProperties(context.Context, *GetServerPropertiesReq) (*GetServerPropertiesResp, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetServerProperties not implemented")
}
func (UnimplementedUIFrameworkServer) SetClearColor(context.Context, *SetClearColorReq) (*SetClearColorResp, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SetClearColor not implemented")
}
func (UnimplementedUIFrameworkServer) mustEmbedUnimplementedUIFrameworkServer() {}

// UnsafeUIFrameworkServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to UIFrameworkServer will
// result in compilation errors.
type UnsafeUIFrameworkServer interface {
	mustEmbedUnimplementedUIFrameworkServer()
}

func RegisterUIFrameworkServer(s grpc.ServiceRegistrar, srv UIFrameworkServer) {
	s.RegisterService(&UIFramework_ServiceDesc, srv)
}

func _UIFramework_Edit_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(EditReq)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(UIFrameworkServer).Edit(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/uif.UIFramework/Edit",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(UIFrameworkServer).Edit(ctx, req.(*EditReq))
	}
	return interceptor(ctx, in, info, handler)
}

func _UIFramework_GetEvents_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(GetEventsReq)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(UIFrameworkServer).GetEvents(m, &uIFrameworkGetEventsServer{stream})
}

type UIFramework_GetEventsServer interface {
	Send(*Event) error
	grpc.ServerStream
}

type uIFrameworkGetEventsServer struct {
	grpc.ServerStream
}

func (x *uIFrameworkGetEventsServer) Send(m *Event) error {
	return x.ServerStream.SendMsg(m)
}

func _UIFramework_GetServerProperties_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetServerPropertiesReq)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(UIFrameworkServer).GetServerProperties(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/uif.UIFramework/GetServerProperties",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(UIFrameworkServer).GetServerProperties(ctx, req.(*GetServerPropertiesReq))
	}
	return interceptor(ctx, in, info, handler)
}

func _UIFramework_SetClearColor_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SetClearColorReq)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(UIFrameworkServer).SetClearColor(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/uif.UIFramework/SetClearColor",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(UIFrameworkServer).SetClearColor(ctx, req.(*SetClearColorReq))
	}
	return interceptor(ctx, in, info, handler)
}

// UIFramework_ServiceDesc is the grpc.ServiceDesc for UIFramework service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var UIFramework_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "uif.UIFramework",
	HandlerType: (*UIFrameworkServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Edit",
			Handler:    _UIFramework_Edit_Handler,
		},
		{
			MethodName: "GetServerProperties",
			Handler:    _UIFramework_GetServerProperties_Handler,
		},
		{
			MethodName: "SetClearColor",
			Handler:    _UIFramework_SetClearColor_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "GetEvents",
			Handler:       _UIFramework_GetEvents_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "uif.proto",
}
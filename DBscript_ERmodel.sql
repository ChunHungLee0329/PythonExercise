/*
檔名:DBscript_ERmodel.sql
版本:version 1.00
功能:demo/implement DB ER model of interview
作者:李俊鴻, Neil Lee
時間:2016/12/30
更新紀錄:(最新的在最上面)
	=== Version 1.01 2016/12/29 update ===
	(1)create basic DB data table and the relative primary key.
作者筆記:
	(1)adding some script to create data
	(2)have some SQL to select/join/calculate data.
*/


IF OBJECT_ID('Order') IS NOT NULL 
BEGIN
	DROP TABLE [Order]
END
CREATE TABLE [Order]
(	
	[OrderNo] [VARCHAR] (20) NOT NULL,
	[WorkOrder] [VARCHAR] (20) NULL,
	[ShipPriority] [INT] NULL, 
	[ShipCarrier] [NVARCHAR] (10) NULL,
	[ShipAddress] [NVARCHAR] (100) NULL,
	[ShipCountry] [NVARCHAR] (20) NULL,
	[ShipPort] [NVARCHAR] (15) NULL,
	CONSTRAINT [PK_Order] PRIMARY KEY CLUSTERED 
	(
		[OrderNo] ASC
	)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)

IF OBJECT_ID('OrderItem') IS NOT NULL 
BEGIN
	DROP TABLE [OrderItem]
END
CREATE TABLE [OrderItem]
(	
	[OrderNo] [VARCHAR] (20) NOT NULL,
	[OrderItem] [VARCHAR] (10) NOT NULL,
	[PartName] [VARCHAR] (20) NULL,
	[OrderQTY] [INT] NULL,
	[OrderStatus] [VARCHAR] (5) NULL, 
	CONSTRAINT [PK_OrderItem] PRIMARY KEY CLUSTERED 
	(
		[OrderNo] ASC, 
		[OrderItem] ASC
	)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)

IF OBJECT_ID('Product') IS NOT NULL 
BEGIN
	DROP TABLE [Product]
END
CREATE TABLE [Product]
(	
	[SalePartName] [VARCHAR] (20) NULL,
	[PartName] [VARCHAR] (20) NOT NULL,
	[ProductModel] [VARCHAR] (10) NULL,
	[Dimension] [VARCHAR] (20) NULL,
	[WeightInfo] [VARCHAR] (20) NULL,
	[UnitPrice] [FLOAT] NULL,
	[Description] [VARCHAR] NULL,
	[BOM] [VARCHAR] NULL, 
	CONSTRAINT [PK_Product] PRIMARY KEY CLUSTERED 
	(
		[PartName] ASC
	)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)

IF OBJECT_ID('Manufacture') IS NOT NULL 
BEGIN
	DROP TABLE [Manufacture]
END
CREATE TABLE [Manufacture]
(
	[WorkOrder] [VARCHAR] (20) NOT NULL,
	[TempSerialNo] [VARCHAR] (25) NOT NULL,
	[SerialNo] [VARCHAR] (25) NULL,
	[PartName] [VARCHAR] (20) NULL,
	[Material] [VARCHAR] (20) NULL,
	[WorkStation] [VARCHAR] (15) NULL,
	[WorkStatus] [VARCHAR] (5) NULL,
	CONSTRAINT [PK_Manufacture] PRIMARY KEY CLUSTERED 
	(
		[WorkOrder] ASC,
		[TempSerialNo] ASC
	)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)

IF OBJECT_ID('MaterialBOM') IS NOT NULL 
BEGIN
	DROP TABLE [MaterialBOM]
END
CREATE TABLE [MaterialBOM]
(
	[PartName] [VARCHAR] (20) NOT NULL,
	[SalePartName] [VARCHAR] (20) NULL,
	[BOM] [VARCHAR] (100) NULL,
	[Material] [VARCHAR] (20) NULL,
	[UnitPrice] [FLOAT] NULL,
	CONSTRAINT [PK_MaterialBOM] PRIMARY KEY CLUSTERED 
	(
		[PartName] ASC
	)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)

IF OBJECT_ID('User') IS NOT NULL 
BEGIN
	DROP TABLE [User]
END
CREATE TABLE [User]
(
	[UserName] [NVARCHAR] (30) NULL,
	[UserID] [VARCHAR] (20) NOT NULL,
	[Password] [VARCHAR] (30) NULL,
	[Email] [VARCHAR] (50) NULL,
	[Dept] [NVARCHAR] (50) NULL,
	[UserLevel] [VARCHAR] (5) NULL,
	CONSTRAINT [PK_User] PRIMARY KEY CLUSTERED 
	(
		[UserID] ASC
	)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)

IF OBJECT_ID('Inventory') IS NOT NULL 
BEGIN
	DROP TABLE [Inventory]
END
CREATE TABLE [Inventory]
(
	[PartName] [VARCHAR] (20) NULL,
	[WareHouse] [NVARCHAR] (20) NULL,
	[Location] [VARCHAR] (20) NULL, 
	[PackageInfo] [VARCHAR] (50) NULL,
	[SerialNo] [VARCHAR] (25) NOT NULL,
	[UpdateDate] [VARCHAR] (12) NULL,
	[UpdateTime] [VARCHAR] (12) NULL,
	CONSTRAINT [PK_Inventory] PRIMARY KEY CLUSTERED 
	(
		[SerialNo] ASC
	)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)

IF OBJECT_ID('ShipmentInfo') IS NOT NULL 
BEGIN
	DROP TABLE [ShipmentInfo]
END
CREATE TABLE [ShipmentInfo]
(
	[ShipmentID] [VARCHAR] (20) NOT NULL,
	[CustomsNo] [VARCHAR] (20) NULL,
	[ShipmentDate] [VARCHAR] (12) NULL,
	[ShipmentQTY] [INT] NULL,
	[ShipmentStatus] [VARCHAR] (5) NULL,
	[UserConfirm] [VARCHAR] (30) NULL,
	CONSTRAINT [PK_ShipmentInfo] PRIMARY KEY CLUSTERED 
	(
		[ShipmentID] ASC
	)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)

IF OBJECT_ID('PalletInfo') IS NOT NULL 
BEGIN
	DROP TABLE [PalletInfo]
END
CREATE TABLE [PalletInfo]
(
	[ShipmentID] [VARCHAR] (20) NULL,
	[OrderNo] [VARCHAR] (20) NULL,
	[OrderItem] [VARCHAR] (10) NULL,
	[PalletID] [VARCHAR] (10) NULL,
	[LayerID] [VARCHAR] (10) NULL,
	[LayerSequence] [VARCHAR] (10) NULL,
	[SerialNo] [VARCHAR] (25) NOT NULL,
	CONSTRAINT [PK_PalletInfo] PRIMARY KEY CLUSTERED 
	(
		[SerialNo] ASC
	)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)



--SELECT TABLE
/*
SELECT * FROM [Order]
SELECT * FROM [OrderItem]
SELECT * FROM [Product]
SELECT * FROM [Manufacture]
SELECT * FROM [MaterialBOM]
SELECT * FROM [User]
SELECT * FROM [Inventory]
SELECT * FROM [ShipmentInfo]
SELECT * FROM [PalletInfo]
*/


--DROP TABLE
/*
DROP TABLE [Order]
DROP TABLE [OrderItem]
DROP TABLE [Product]
DROP TABLE [Manufacture]
DROP TABLE [MaterialBOM]
DROP TABLE [User]
DROP TABLE [Inventory]
DROP TABLE [ShipmentInfo]
DROP TABLE [PalletInfo]
*/
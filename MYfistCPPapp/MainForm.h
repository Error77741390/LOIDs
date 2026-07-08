#pragma once

#define NOMINMAX
#include <windows.h>
#include <mmsystem.h>
#include <atomic>
#pragma comment(lib, "winmm.lib")

namespace MYfistCPPapp {

	using namespace System;
	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Windows::Forms;
	using namespace System::Data;
	using namespace System::Drawing;

	public ref class MainForm : public System::Windows::Forms::Form
	{
	public:
		MainForm(void)
		{
			InitializeComponent();
		}

	protected:
		~MainForm()
		{
			if (components)
			{
				delete components;
			}
		}
	private: System::Windows::Forms::Button^ button1;
	private: System::Windows::Forms::Panel^ headerPanel;
	private: System::Drawing::Point dragOffset;
	private: bool isDragging;
	private: System::Windows::Forms::FlowLayoutPanel^ menu_btn_holder;
	private: System::Windows::Forms::Panel^ home;
	private: System::Windows::Forms::Panel^ about;
	private: System::Windows::Forms::Label^ about_label;
	private: System::Windows::Forms::Label^ label1;
	private: System::Windows::Forms::Button^ button4;
	private: System::Windows::Forms::Button^ button2;
	private: System::Windows::Forms::Button^ button3;
	private: System::Windows::Forms::Panel^ settings;
	private: System::Windows::Forms::Label^ label3;
	private: System::Windows::Forms::Button^ button5;
	private: System::Windows::Forms::CheckBox^ topmost_toggle;
	private: System::Windows::Forms::Label^ label4;
	private: System::Windows::Forms::Label^ label5;
	private: System::Windows::Forms::Label^ contact_label;
	private: System::Windows::Forms::Label^ mydiscord;
	private: System::Windows::Forms::ComboBox^ comboBox1;
	private: System::Windows::Forms::Label^ label2;

	private: System::Windows::Forms::Label^ statusLabel;
	private: System::Windows::Forms::Button^ toggleButton;
	private: System::Windows::Forms::Label^ liveCpsLabel;
	private: System::Windows::Forms::Label^ totalClicksLabel;
	private: System::Windows::Forms::Timer^ statsTimer;
	private: System::ComponentModel::IContainer^ statsTimerContainer;

	private:
		static const int TOGGLE_HOTKEY_ID = 9001;
		int m_spamKeyVk = 'F';       // Default key to spam
		int m_toggleKeyVk = VK_F6;   // Default toggle hotkey

		Object^ m_lock = gcnew Object();
		bool m_active = false;
		bool m_running = true;
		int m_cps = 250;
		long long m_totalClicks = 0;
		int m_sampleClicks = 0;
		long long m_lastQpc = 0;
		long long m_qpcFreq = 0;
		System::Threading::Thread^ m_clickThread;

	private: System::Windows::Forms::TextBox^ keybind_txtbox;
	private: System::Windows::Forms::Label^ tglKeybind_label;
	private: System::Windows::Forms::TextBox^ textBox1;
	private: System::Windows::Forms::Label^ label6;
	private: System::Windows::Forms::Button^ button6;
	private: System::ComponentModel::IContainer^ components;

#pragma region Windows Form Designer generated code
		   void InitializeComponent(void)
		   {
			   this->components = (gcnew System::ComponentModel::Container());
			   System::ComponentModel::ComponentResourceManager^ resources = (gcnew System::ComponentModel::ComponentResourceManager(MainForm::typeid));
			   this->button1 = (gcnew System::Windows::Forms::Button());
			   this->headerPanel = (gcnew System::Windows::Forms::Panel());
			   this->button5 = (gcnew System::Windows::Forms::Button());
			   this->button4 = (gcnew System::Windows::Forms::Button());
			   this->menu_btn_holder = (gcnew System::Windows::Forms::FlowLayoutPanel());
			   this->button3 = (gcnew System::Windows::Forms::Button());
			   this->button2 = (gcnew System::Windows::Forms::Button());
			   this->home = (gcnew System::Windows::Forms::Panel());
			   this->label1 = (gcnew System::Windows::Forms::Label());
			   this->statusLabel = (gcnew System::Windows::Forms::Label());
			   this->toggleButton = (gcnew System::Windows::Forms::Button());
			   this->liveCpsLabel = (gcnew System::Windows::Forms::Label());
			   this->totalClicksLabel = (gcnew System::Windows::Forms::Label());
			   this->about = (gcnew System::Windows::Forms::Panel());
			   this->contact_label = (gcnew System::Windows::Forms::Label());
			   this->mydiscord = (gcnew System::Windows::Forms::Label());
			   this->label5 = (gcnew System::Windows::Forms::Label());
			   this->about_label = (gcnew System::Windows::Forms::Label());
			   this->settings = (gcnew System::Windows::Forms::Panel());
			   this->textBox1 = (gcnew System::Windows::Forms::TextBox());
			   this->label6 = (gcnew System::Windows::Forms::Label());
			   this->keybind_txtbox = (gcnew System::Windows::Forms::TextBox());
			   this->tglKeybind_label = (gcnew System::Windows::Forms::Label());
			   this->label2 = (gcnew System::Windows::Forms::Label());
			   this->comboBox1 = (gcnew System::Windows::Forms::ComboBox());
			   this->label4 = (gcnew System::Windows::Forms::Label());
			   this->topmost_toggle = (gcnew System::Windows::Forms::CheckBox());
			   this->label3 = (gcnew System::Windows::Forms::Label());
			   this->statsTimer = (gcnew System::Windows::Forms::Timer(this->components));
			   this->button6 = (gcnew System::Windows::Forms::Button());
			   this->headerPanel->SuspendLayout();
			   this->menu_btn_holder->SuspendLayout();
			   this->home->SuspendLayout();
			   this->about->SuspendLayout();
			   this->settings->SuspendLayout();
			   this->SuspendLayout();
			   // 
			   // button1
			   // 
			   this->button1->BackColor = System::Drawing::Color::FromArgb(static_cast<System::Int32>(static_cast<System::Byte>(17)), static_cast<System::Int32>(static_cast<System::Byte>(15)),
				   static_cast<System::Int32>(static_cast<System::Byte>(17)));
			   this->button1->BackgroundImage = (cli::safe_cast<System::Drawing::Image^>(resources->GetObject(L"button1.BackgroundImage")));
			   this->button1->BackgroundImageLayout = System::Windows::Forms::ImageLayout::Center;
			   this->button1->Cursor = System::Windows::Forms::Cursors::Hand;
			   this->button1->FlatAppearance->BorderColor = System::Drawing::Color::Black;
			   this->button1->FlatStyle = System::Windows::Forms::FlatStyle::Flat;
			   this->button1->ForeColor = System::Drawing::Color::Black;
			   this->button1->Location = System::Drawing::Point(4, 4);
			   this->button1->Margin = System::Windows::Forms::Padding(4);
			   this->button1->Name = L"button1";
			   this->button1->Size = System::Drawing::Size(60, 60);
			   this->button1->TabIndex = 0;
			   this->button1->UseVisualStyleBackColor = false;
			   this->button1->Click += gcnew System::EventHandler(this, &MainForm::button1_Click);
			   // 
			   // headerPanel
			   // 
			   this->headerPanel->BackColor = System::Drawing::Color::FromArgb(static_cast<System::Int32>(static_cast<System::Byte>(17)), static_cast<System::Int32>(static_cast<System::Byte>(15)),
				   static_cast<System::Int32>(static_cast<System::Byte>(17)));
			   this->headerPanel->Controls->Add(this->button5);
			   this->headerPanel->Controls->Add(this->button4);
			   this->headerPanel->Cursor = System::Windows::Forms::Cursors::Cross;
			   this->headerPanel->Dock = System::Windows::Forms::DockStyle::Top;
			   this->headerPanel->Location = System::Drawing::Point(0, 0);
			   this->headerPanel->Margin = System::Windows::Forms::Padding(0);
			   this->headerPanel->Name = L"headerPanel";
			   this->headerPanel->Size = System::Drawing::Size(579, 49);
			   this->headerPanel->TabIndex = 0;
			   this->headerPanel->MouseDown += gcnew System::Windows::Forms::MouseEventHandler(this, &MainForm::headerPanel_MouseDown);
			   this->headerPanel->MouseMove += gcnew System::Windows::Forms::MouseEventHandler(this, &MainForm::headerPanel_MouseMove);
			   this->headerPanel->MouseUp += gcnew System::Windows::Forms::MouseEventHandler(this, &MainForm::headerPanel_MouseUp);
			   // 
			   // button5
			   // 
			   this->button5->BackColor = System::Drawing::Color::FromArgb(static_cast<System::Int32>(static_cast<System::Byte>(17)), static_cast<System::Int32>(static_cast<System::Byte>(15)),
				   static_cast<System::Int32>(static_cast<System::Byte>(17)));
			   this->button5->BackgroundImage = (cli::safe_cast<System::Drawing::Image^>(resources->GetObject(L"button5.BackgroundImage")));
			   this->button5->BackgroundImageLayout = System::Windows::Forms::ImageLayout::Zoom;
			   this->button5->Cursor = System::Windows::Forms::Cursors::Hand;
			   this->button5->FlatAppearance->BorderColor = System::Drawing::Color::Black;
			   this->button5->FlatStyle = System::Windows::Forms::FlatStyle::Flat;
			   this->button5->ForeColor = System::Drawing::Color::Black;
			   this->button5->Location = System::Drawing::Point(472, 4);
			   this->button5->Margin = System::Windows::Forms::Padding(4);
			   this->button5->Name = L"button5";
			   this->button5->Size = System::Drawing::Size(43, 42);
			   this->button5->TabIndex = 6;
			   this->button5->UseVisualStyleBackColor = false;
			   this->button5->Click += gcnew System::EventHandler(this, &MainForm::button5_Click);
			   // 
			   // button4
			   // 
			   this->button4->BackColor = System::Drawing::Color::FromArgb(static_cast<System::Int32>(static_cast<System::Byte>(17)), static_cast<System::Int32>(static_cast<System::Byte>(15)),
				   static_cast<System::Int32>(static_cast<System::Byte>(17)));
			   this->button4->BackgroundImage = (cli::safe_cast<System::Drawing::Image^>(resources->GetObject(L"button4.BackgroundImage")));
			   this->button4->BackgroundImageLayout = System::Windows::Forms::ImageLayout::Zoom;
			   this->button4->Cursor = System::Windows::Forms::Cursors::Hand;
			   this->button4->FlatAppearance->BorderColor = System::Drawing::Color::Black;
			   this->button4->FlatStyle = System::Windows::Forms::FlatStyle::Flat;
			   this->button4->ForeColor = System::Drawing::Color::Black;
			   this->button4->Location = System::Drawing::Point(523, 4);
			   this->button4->Margin = System::Windows::Forms::Padding(4);
			   this->button4->Name = L"button4";
			   this->button4->Size = System::Drawing::Size(43, 42);
			   this->button4->TabIndex = 5;
			   this->button4->UseVisualStyleBackColor = false;
			   this->button4->Click += gcnew System::EventHandler(this, &MainForm::button4_Click);
			   // 
			   // menu_btn_holder
			   // 
			   this->menu_btn_holder->AccessibleRole = System::Windows::Forms::AccessibleRole::MenuBar;
			   this->menu_btn_holder->Anchor = System::Windows::Forms::AnchorStyles::Top;
			   this->menu_btn_holder->AutoSizeMode = System::Windows::Forms::AutoSizeMode::GrowAndShrink;
			   this->menu_btn_holder->BackColor = System::Drawing::Color::FromArgb(static_cast<System::Int32>(static_cast<System::Byte>(17)), static_cast<System::Int32>(static_cast<System::Byte>(15)),
				   static_cast<System::Int32>(static_cast<System::Byte>(17)));
			   this->menu_btn_holder->Controls->Add(this->button1);
			   this->menu_btn_holder->Controls->Add(this->button3);
			   this->menu_btn_holder->Controls->Add(this->button2);
			   this->menu_btn_holder->FlowDirection = System::Windows::Forms::FlowDirection::TopDown;
			   this->menu_btn_holder->Location = System::Drawing::Point(15, 66);
			   this->menu_btn_holder->Margin = System::Windows::Forms::Padding(4);
			   this->menu_btn_holder->Name = L"menu_btn_holder";
			   this->menu_btn_holder->Size = System::Drawing::Size(70, 205);
			   this->menu_btn_holder->TabIndex = 3;
			   this->menu_btn_holder->WrapContents = false;
			   // 
			   // button3
			   // 
			   this->button3->BackColor = System::Drawing::Color::FromArgb(static_cast<System::Int32>(static_cast<System::Byte>(17)), static_cast<System::Int32>(static_cast<System::Byte>(15)),
				   static_cast<System::Int32>(static_cast<System::Byte>(17)));
			   this->button3->BackgroundImage = (cli::safe_cast<System::Drawing::Image^>(resources->GetObject(L"button3.BackgroundImage")));
			   this->button3->BackgroundImageLayout = System::Windows::Forms::ImageLayout::Center;
			   this->button3->Cursor = System::Windows::Forms::Cursors::Hand;
			   this->button3->FlatAppearance->BorderColor = System::Drawing::Color::Black;
			   this->button3->FlatStyle = System::Windows::Forms::FlatStyle::Flat;
			   this->button3->ForeColor = System::Drawing::Color::Black;
			   this->button3->Location = System::Drawing::Point(4, 72);
			   this->button3->Margin = System::Windows::Forms::Padding(4);
			   this->button3->Name = L"button3";
			   this->button3->Size = System::Drawing::Size(60, 60);
			   this->button3->TabIndex = 4;
			   this->button3->UseVisualStyleBackColor = false;
			   this->button3->Click += gcnew System::EventHandler(this, &MainForm::button3_Click);
			   // 
			   // button2
			   // 
			   this->button2->BackColor = System::Drawing::Color::FromArgb(static_cast<System::Int32>(static_cast<System::Byte>(17)), static_cast<System::Int32>(static_cast<System::Byte>(15)),
				   static_cast<System::Int32>(static_cast<System::Byte>(17)));
			   this->button2->BackgroundImage = (cli::safe_cast<System::Drawing::Image^>(resources->GetObject(L"button2.BackgroundImage")));
			   this->button2->BackgroundImageLayout = System::Windows::Forms::ImageLayout::Center;
			   this->button2->Cursor = System::Windows::Forms::Cursors::Hand;
			   this->button2->FlatAppearance->BorderColor = System::Drawing::Color::Black;
			   this->button2->FlatStyle = System::Windows::Forms::FlatStyle::Flat;
			   this->button2->ForeColor = System::Drawing::Color::Black;
			   this->button2->Location = System::Drawing::Point(4, 140);
			   this->button2->Margin = System::Windows::Forms::Padding(4);
			   this->button2->Name = L"button2";
			   this->button2->Size = System::Drawing::Size(60, 60);
			   this->button2->TabIndex = 3;
			   this->button2->UseVisualStyleBackColor = false;
			   this->button2->Click += gcnew System::EventHandler(this, &MainForm::button2_Click);
			   // 
			   // home
			   // 
			   this->home->BackColor = System::Drawing::Color::Black;
			   this->home->Controls->Add(this->label1);
			   this->home->Controls->Add(this->statusLabel);
			   this->home->Controls->Add(this->toggleButton);
			   this->home->Controls->Add(this->liveCpsLabel);
			   this->home->Controls->Add(this->totalClicksLabel);
			   this->home->Location = System::Drawing::Point(93, 60);
			   this->home->Margin = System::Windows::Forms::Padding(4);
			   this->home->Name = L"home";
			   this->home->Size = System::Drawing::Size(469, 215);
			   this->home->TabIndex = 4;
			   // 
			   // label1
			   // 
			   this->label1->AutoSize = true;
			   this->label1->FlatStyle = System::Windows::Forms::FlatStyle::Flat;
			   this->label1->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 8.25F, static_cast<System::Drawing::FontStyle>((System::Drawing::FontStyle::Bold | System::Drawing::FontStyle::Italic)),
				   System::Drawing::GraphicsUnit::Point, static_cast<System::Byte>(0)));
			   this->label1->ForeColor = System::Drawing::SystemColors::ControlLightLight;
			   this->label1->Location = System::Drawing::Point(11, 14);
			   this->label1->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->label1->Name = L"label1";
			   this->label1->Size = System::Drawing::Size(49, 17);
			   this->label1->TabIndex = 0;
			   this->label1->Text = L"Home";
			   // 
			   // statusLabel
			   // 
			   this->statusLabel->AutoSize = true;
			   this->statusLabel->Font = (gcnew System::Drawing::Font(L"Segoe UI", 14, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(0)));
			   this->statusLabel->ForeColor = System::Drawing::Color::OrangeRed;
			   this->statusLabel->Location = System::Drawing::Point(11, 45);
			   this->statusLabel->Name = L"statusLabel";
			   this->statusLabel->Size = System::Drawing::Size(65, 32);
			   this->statusLabel->TabIndex = 10;
			   this->statusLabel->Text = L"IDLE";
			   // 
			   // toggleButton
			   // 
			   this->toggleButton->BackColor = System::Drawing::Color::FromArgb(static_cast<System::Int32>(static_cast<System::Byte>(30)), static_cast<System::Int32>(static_cast<System::Byte>(30)),
				   static_cast<System::Int32>(static_cast<System::Byte>(34)));
			   this->toggleButton->Cursor = System::Windows::Forms::Cursors::Hand;
			   this->toggleButton->FlatStyle = System::Windows::Forms::FlatStyle::Flat;
			   this->toggleButton->Font = (gcnew System::Drawing::Font(L"Segoe UI", 10, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(0)));
			   this->toggleButton->ForeColor = System::Drawing::Color::White;
			   this->toggleButton->Location = System::Drawing::Point(11, 85);
			   this->toggleButton->Name = L"toggleButton";
			   this->toggleButton->Size = System::Drawing::Size(200, 40);
			   this->toggleButton->TabIndex = 11;
			   this->toggleButton->Text = L"START   [F6]";
			   this->toggleButton->UseVisualStyleBackColor = false;
			   this->toggleButton->Click += gcnew System::EventHandler(this, &MainForm::toggleButton_Click);
			   // 
			   // liveCpsLabel
			   // 
			   this->liveCpsLabel->AutoSize = true;
			   this->liveCpsLabel->Font = (gcnew System::Drawing::Font(L"Segoe UI", 9, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(0)));
			   this->liveCpsLabel->ForeColor = System::Drawing::Color::Gainsboro;
			   this->liveCpsLabel->Location = System::Drawing::Point(11, 140);
			   this->liveCpsLabel->Name = L"liveCpsLabel";
			   this->liveCpsLabel->Size = System::Drawing::Size(79, 20);
			   this->liveCpsLabel->TabIndex = 12;
			   this->liveCpsLabel->Text = L"Live CPS: 0";
			   // 
			   // totalClicksLabel
			   // 
			   this->totalClicksLabel->AutoSize = true;
			   this->totalClicksLabel->Font = (gcnew System::Drawing::Font(L"Segoe UI", 9, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(0)));
			   this->totalClicksLabel->ForeColor = System::Drawing::Color::Gainsboro;
			   this->totalClicksLabel->Location = System::Drawing::Point(11, 162);
			   this->totalClicksLabel->Name = L"totalClicksLabel";
			   this->totalClicksLabel->Size = System::Drawing::Size(98, 20);
			   this->totalClicksLabel->TabIndex = 13;
			   this->totalClicksLabel->Text = L"Total Clicks: 0";
			   // 
			   // about
			   // 
			   this->about->BackColor = System::Drawing::Color::Black;
			   this->about->Controls->Add(this->contact_label);
			   this->about->Controls->Add(this->mydiscord);
			   this->about->Controls->Add(this->label5);
			   this->about->Controls->Add(this->about_label);
			   this->about->Location = System::Drawing::Point(101, 60);
			   this->about->Margin = System::Windows::Forms::Padding(4);
			   this->about->Name = L"about";
			   this->about->Size = System::Drawing::Size(501, 280);
			   this->about->TabIndex = 5;
			   // 
			   // contact_label
			   // 
			   this->contact_label->AutoSize = true;
			   this->contact_label->FlatStyle = System::Windows::Forms::FlatStyle::Flat;
			   this->contact_label->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 8.25F, static_cast<System::Drawing::FontStyle>((System::Drawing::FontStyle::Bold | System::Drawing::FontStyle::Italic)),
				   System::Drawing::GraphicsUnit::Point, static_cast<System::Byte>(0)));
			   this->contact_label->ForeColor = System::Drawing::SystemColors::ControlLightLight;
			   this->contact_label->Location = System::Drawing::Point(9, 107);
			   this->contact_label->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->contact_label->Name = L"contact_label";
			   this->contact_label->Size = System::Drawing::Size(93, 17);
			   this->contact_label->TabIndex = 6;
			   this->contact_label->Text = L"Contact me!";
			   // 
			   // mydiscord
			   // 
			   this->mydiscord->Cursor = System::Windows::Forms::Cursors::IBeam;
			   this->mydiscord->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 10.8F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(0)));
			   this->mydiscord->ForeColor = System::Drawing::SystemColors::ButtonFace;
			   this->mydiscord->Location = System::Drawing::Point(12, 124);
			   this->mydiscord->Name = L"mydiscord";
			   this->mydiscord->Size = System::Drawing::Size(370, 32);
			   this->mydiscord->TabIndex = 1;
			   this->mydiscord->Text = L"Discord - \"simplyloid\"";
			   this->mydiscord->TextAlign = System::Drawing::ContentAlignment::MiddleLeft;
			   // 
			   // label5
			   // 
			   this->label5->Cursor = System::Windows::Forms::Cursors::IBeam;
			   this->label5->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 10.8F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(0)));
			   this->label5->ForeColor = System::Drawing::SystemColors::ButtonFace;
			   this->label5->Location = System::Drawing::Point(-20, 31);
			   this->label5->Name = L"label5";
			   this->label5->Size = System::Drawing::Size(466, 65);
			   this->label5->TabIndex = 4;
			   this->label5->Text = L"I ask of you to not distribute or give to anyone without my permission first!!";
			   this->label5->TextAlign = System::Drawing::ContentAlignment::MiddleCenter;
			   // 
			   // about_label
			   // 
			   this->about_label->AutoSize = true;
			   this->about_label->FlatStyle = System::Windows::Forms::FlatStyle::Flat;
			   this->about_label->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 8.25F, static_cast<System::Drawing::FontStyle>((System::Drawing::FontStyle::Bold | System::Drawing::FontStyle::Italic)),
				   System::Drawing::GraphicsUnit::Point, static_cast<System::Byte>(0)));
			   this->about_label->ForeColor = System::Drawing::SystemColors::ControlLightLight;
			   this->about_label->Location = System::Drawing::Point(4, 14);
			   this->about_label->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->about_label->Name = L"about_label";
			   this->about_label->Size = System::Drawing::Size(50, 17);
			   this->about_label->TabIndex = 0;
			   this->about_label->Text = L"About";
			   // 
			   // settings
			   // 
			   this->settings->Anchor = System::Windows::Forms::AnchorStyles::Top;
			   this->settings->BackColor = System::Drawing::Color::Black;
			   this->settings->Controls->Add(this->button6);
			   this->settings->Controls->Add(this->textBox1);
			   this->settings->Controls->Add(this->label6);
			   this->settings->Controls->Add(this->keybind_txtbox);
			   this->settings->Controls->Add(this->tglKeybind_label);
			   this->settings->Controls->Add(this->label2);
			   this->settings->Controls->Add(this->comboBox1);
			   this->settings->Controls->Add(this->label4);
			   this->settings->Controls->Add(this->topmost_toggle);
			   this->settings->Controls->Add(this->label3);
			   this->settings->Location = System::Drawing::Point(89, 60);
			   this->settings->Margin = System::Windows::Forms::Padding(4);
			   this->settings->Name = L"settings";
			   this->settings->Size = System::Drawing::Size(521, 304);
			   this->settings->TabIndex = 6;
			   // 
			   // textBox1
			   // 
			   this->textBox1->Location = System::Drawing::Point(90, 138);
			   this->textBox1->MaxLength = 1;
			   this->textBox1->Name = L"textBox1";
			   this->textBox1->Size = System::Drawing::Size(35, 22);
			   this->textBox1->TabIndex = 13;
			   this->textBox1->TabStop = false;
			   this->textBox1->Text = L"f";
			   this->textBox1->TextAlign = System::Windows::Forms::HorizontalAlignment::Center;
			   this->textBox1->WordWrap = false;
			   this->textBox1->KeyDown += gcnew System::Windows::Forms::KeyEventHandler(this, &MainForm::textBox1_KeyDown);
			   // 
			   // label6
			   // 
			   this->label6->AutoSize = true;
			   this->label6->ForeColor = System::Drawing::Color::White;
			   this->label6->Location = System::Drawing::Point(16, 143);
			   this->label6->Name = L"label6";
			   this->label6->Size = System::Drawing::Size(69, 16);
			   this->label6->TabIndex = 12;
			   this->label6->Text = L"Key Spam";
			   // 
			   // keybind_txtbox
			   // 
			   this->keybind_txtbox->Location = System::Drawing::Point(124, 109);
			   this->keybind_txtbox->MaxLength = 1;
			   this->keybind_txtbox->Name = L"keybind_txtbox";
			   this->keybind_txtbox->Size = System::Drawing::Size(35, 22);
			   this->keybind_txtbox->TabIndex = 11;
			   this->keybind_txtbox->TabStop = false;
			   this->keybind_txtbox->Text = L"Q";
			   this->keybind_txtbox->TextAlign = System::Windows::Forms::HorizontalAlignment::Center;
			   this->keybind_txtbox->WordWrap = false;
			   this->keybind_txtbox->KeyDown += gcnew System::Windows::Forms::KeyEventHandler(this, &MainForm::keybind_txtbox_KeyDown);
			   // 
			   // tglKeybind_label
			   // 
			   this->tglKeybind_label->AutoSize = true;
			   this->tglKeybind_label->ForeColor = System::Drawing::Color::White;
			   this->tglKeybind_label->Location = System::Drawing::Point(15, 114);
			   this->tglKeybind_label->Name = L"tglKeybind_label";
			   this->tglKeybind_label->Size = System::Drawing::Size(103, 16);
			   this->tglKeybind_label->TabIndex = 10;
			   this->tglKeybind_label->Text = L"Toggle Keybind";
			   // 
			   // label2
			   // 
			   this->label2->AutoSize = true;
			   this->label2->FlatStyle = System::Windows::Forms::FlatStyle::Flat;
			   this->label2->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 8.25F, static_cast<System::Drawing::FontStyle>((System::Drawing::FontStyle::Bold | System::Drawing::FontStyle::Italic)),
				   System::Drawing::GraphicsUnit::Point, static_cast<System::Byte>(0)));
			   this->label2->ForeColor = System::Drawing::SystemColors::ControlLightLight;
			   this->label2->Location = System::Drawing::Point(386, 14);
			   this->label2->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->label2->Name = L"label2";
			   this->label2->Size = System::Drawing::Size(70, 17);
			   this->label2->TabIndex = 9;
			   this->label2->Text = L"ver - 0.1";
			   // 
			   // comboBox1
			   // 
			   this->comboBox1->BackColor = System::Drawing::Color::White;
			   this->comboBox1->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 7.8F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(0)));
			   this->comboBox1->FormattingEnabled = true;
			   this->comboBox1->Items->AddRange(gcnew cli::array< System::Object^  >(5) { L"100", L"250", L"300", L"500", L"999" });
			   this->comboBox1->Location = System::Drawing::Point(57, 82);
			   this->comboBox1->MaxLength = 3;
			   this->comboBox1->Name = L"comboBox1";
			   this->comboBox1->Size = System::Drawing::Size(63, 24);
			   this->comboBox1->TabIndex = 8;
			   this->comboBox1->Text = L"250";
			   this->comboBox1->SelectedIndexChanged += gcnew System::EventHandler(this, &MainForm::comboBox1_SelectedIndexChanged);
			   this->comboBox1->TextChanged += gcnew System::EventHandler(this, &MainForm::comboBox1_SelectedIndexChanged);
			   // 
			   // label4
			   // 
			   this->label4->AutoSize = true;
			   this->label4->ForeColor = System::Drawing::SystemColors::ButtonFace;
			   this->label4->Location = System::Drawing::Point(18, 88);
			   this->label4->Name = L"label4";
			   this->label4->Size = System::Drawing::Size(34, 16);
			   this->label4->TabIndex = 3;
			   this->label4->Text = L"CPS";
			   // 
			   // topmost_toggle
			   // 
			   this->topmost_toggle->AutoSize = true;
			   this->topmost_toggle->CheckAlign = System::Drawing::ContentAlignment::MiddleRight;
			   this->topmost_toggle->Checked = true;
			   this->topmost_toggle->CheckState = System::Windows::Forms::CheckState::Checked;
			   this->topmost_toggle->Cursor = System::Windows::Forms::Cursors::Hand;
			   this->topmost_toggle->ForeColor = System::Drawing::Color::White;
			   this->topmost_toggle->Location = System::Drawing::Point(18, 56);
			   this->topmost_toggle->Name = L"topmost_toggle";
			   this->topmost_toggle->Size = System::Drawing::Size(83, 20);
			   this->topmost_toggle->TabIndex = 1;
			   this->topmost_toggle->Text = L"TopMost";
			   this->topmost_toggle->UseVisualStyleBackColor = true;
			   this->topmost_toggle->CheckedChanged += gcnew System::EventHandler(this, &MainForm::topmost_toggle_CheckedChanged);
			   // 
			   // label3
			   // 
			   this->label3->AutoSize = true;
			   this->label3->FlatStyle = System::Windows::Forms::FlatStyle::Flat;
			   this->label3->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 8.25F, static_cast<System::Drawing::FontStyle>((System::Drawing::FontStyle::Bold | System::Drawing::FontStyle::Italic)),
				   System::Drawing::GraphicsUnit::Point, static_cast<System::Byte>(0)));
			   this->label3->ForeColor = System::Drawing::SystemColors::ControlLightLight;
			   this->label3->Location = System::Drawing::Point(15, 14);
			   this->label3->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->label3->Name = L"label3";
			   this->label3->Size = System::Drawing::Size(67, 17);
			   this->label3->TabIndex = 0;
			   this->label3->Text = L"Settings";
			   // 
			   // statsTimer
			   // 
			   this->statsTimer->Interval = 250;
			   this->statsTimer->Tick += gcnew System::EventHandler(this, &MainForm::statsTimer_Tick);
			   // 
			   // button6
			   // 
			   this->button6->Location = System::Drawing::Point(131, 137);
			   this->button6->Name = L"button6";
			   this->button6->Size = System::Drawing::Size(50, 22);
			   this->button6->TabIndex = 14;
			   this->button6->Text = L"LMB";
			   this->button6->UseVisualStyleBackColor = true;
			   // 
			   // MainForm
			   // 
			   this->AutoScaleDimensions = System::Drawing::SizeF(8, 16);
			   this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			   this->BackColor = System::Drawing::Color::Black;
			   this->ClientSize = System::Drawing::Size(579, 290);
			   this->ControlBox = false;
			   this->Controls->Add(this->menu_btn_holder);
			   this->Controls->Add(this->headerPanel);
			   this->Controls->Add(this->about);
			   this->Controls->Add(this->settings);
			   this->Controls->Add(this->home);
			   this->ForeColor = System::Drawing::SystemColors::ControlText;
			   this->FormBorderStyle = System::Windows::Forms::FormBorderStyle::None;
			   this->Margin = System::Windows::Forms::Padding(3, 2, 3, 2);
			   this->MaximizeBox = false;
			   this->Name = L"MainForm";
			   this->StartPosition = System::Windows::Forms::FormStartPosition::CenterScreen;
			   this->Text = L"MainWindow";
			   this->TopMost = true;
			   this->TransparencyKey = System::Drawing::Color::RosyBrown;
			   this->FormClosing += gcnew System::Windows::Forms::FormClosingEventHandler(this, &MainForm::MainForm_FormClosing);
			   this->Load += gcnew System::EventHandler(this, &MainForm::MainForm_Load);
			   this->headerPanel->ResumeLayout(false);
			   this->menu_btn_holder->ResumeLayout(false);
			   this->home->ResumeLayout(false);
			   this->home->PerformLayout();
			   this->about->ResumeLayout(false);
			   this->about->PerformLayout();
			   this->settings->ResumeLayout(false);
			   this->settings->PerformLayout();
			   this->ResumeLayout(false);

		   }
#pragma endregion

	protected:
		virtual void WndProc(System::Windows::Forms::Message% m) override {
			if (m.Msg == WM_HOTKEY && (int)m.WParam == TOGGLE_HOTKEY_ID) {
				ToggleMacro();
			}
			System::Windows::Forms::Form::WndProc(m);
		}

	private: System::Void button3_Click(System::Object^ sender, System::EventArgs^ e) {
		this->home->Visible = false;
		this->about->Visible = true;
		this->settings->Visible = false;
	}
	private: System::Void button2_Click(System::Object^ sender, System::EventArgs^ e) {
		this->home->Visible = false;
		this->about->Visible = false;
		this->settings->Visible = true;
	}
	private: System::Void headerPanel_MouseDown(System::Object^ sender, System::Windows::Forms::MouseEventArgs^ e) {
		if (e->Button == System::Windows::Forms::MouseButtons::Left) {
			isDragging = true;
			dragOffset = System::Drawing::Point(e->X, e->Y);
		}
	}
	private: System::Void headerPanel_MouseMove(System::Object^ sender, System::Windows::Forms::MouseEventArgs^ e) {
		if (isDragging) {
			System::Drawing::Point mousePos = Control::MousePosition;
			this->Location = System::Drawing::Point(mousePos.X - dragOffset.X, mousePos.Y - dragOffset.Y);
		}
	}
	private: System::Void headerPanel_MouseUp(System::Object^ sender, System::Windows::Forms::MouseEventArgs^ e) {
		isDragging = false;
	}
	private: System::Void button1_Click(System::Object^ sender, System::EventArgs^ e) {
		this->home->Visible = true;
		this->about->Visible = false;
		this->settings->Visible = false;
	}
	private: System::Void button4_Click(System::Object^ sender, System::EventArgs^ e) {
		Application::Exit();
	}
	private: System::Void button5_Click(System::Object^ sender, System::EventArgs^ e) {
		this->WindowState = System::Windows::Forms::FormWindowState::Minimized;
	}
	private: System::Void topmost_toggle_CheckedChanged(System::Object^ sender, System::EventArgs^ e) {
		this->TopMost = this->topmost_toggle->Checked;
	}

		   // Dynamic global hotkey re-registration system
	private: void UpdateGlobalHotkey(int vkCode, System::String^ keyDisplay) {
		HWND hwnd = (HWND)(this->Handle.ToPointer());
		UnregisterHotKey(hwnd, TOGGLE_HOTKEY_ID);

		m_toggleKeyVk = vkCode;
		RegisterHotKey(hwnd, TOGGLE_HOTKEY_ID, MOD_NOREPEAT, m_toggleKeyVk);

		// Instantly update the home UI visual label context
		System::String^ cleanStr = keyDisplay->ToUpper();
		if (m_active) {
			this->toggleButton->Text = L"\u25A0  STOP    [" + cleanStr + L"]";
		}
		else {
			this->toggleButton->Text = L"\u25B6  START   [" + cleanStr + L"]";
		}
	}

	private: System::Void keybind_txtbox_KeyDown(System::Object^ sender, System::Windows::Forms::KeyEventArgs^ e) {
		if (e->KeyCode != System::Windows::Forms::Keys::Back && e->KeyCode != System::Windows::Forms::Keys::Delete) {
			char ch = KeyCodeToChar(e->KeyCode);
			if (ch != ' ') {
				wchar_t wch = (wchar_t)ch;
				System::String^ textStr = gcnew System::String(&wch, 0, 1);
				keybind_txtbox->Text = textStr;

				int vk = CharToVkCode(ch);
				UpdateGlobalHotkey(vk, textStr);
			}
			else {
				// Handle Function Keys (like F1-F12) explicitly if pressed
				if (e->KeyCode >= System::Windows::Forms::Keys::F1 && e->KeyCode <= System::Windows::Forms::Keys::F12) {
					System::String^ fKeyStr = e->KeyCode.ToString();
					keybind_txtbox->Text = fKeyStr;
					UpdateGlobalHotkey((int)e->KeyCode, fKeyStr);
				}
			}
			e->Handled = true;
			e->SuppressKeyPress = true;
		}
	}

	private: System::Void textBox1_KeyDown(System::Object^ sender, System::Windows::Forms::KeyEventArgs^ e) {
		if (e->KeyCode != System::Windows::Forms::Keys::Back && e->KeyCode != System::Windows::Forms::Keys::Delete) {
			char ch = KeyCodeToChar(e->KeyCode);
			if (ch != ' ') {
				wchar_t wch = (wchar_t)ch;
				textBox1->Text = gcnew System::String(&wch, 0, 1);

				System::Threading::Monitor::Enter(m_lock);
				try {
					m_spamKeyVk = CharToVkCode(ch);
				}
				finally {
					System::Threading::Monitor::Exit(m_lock);
				}
			}
			e->Handled = true;
			e->SuppressKeyPress = true;
		}
	}

	private: void UpdateCpsFromComboBox() {
		int val;
		if (System::Int32::TryParse(this->comboBox1->Text, val)) {
			if (val < 1) val = 1;
			if (val > 999) val = 999;
			System::Threading::Monitor::Enter(m_lock);
			try {
				m_cps = val;
			}
			finally {
				System::Threading::Monitor::Exit(m_lock);
			}
		}
	}
	private: System::Void comboBox1_SelectedIndexChanged(System::Object^ sender, System::EventArgs^ e) {
		UpdateCpsFromComboBox();
	}

	private: int CharToVkCode(char ch) {
		if (ch >= 'A' && ch <= 'Z') return (int)ch;
		if (ch >= 'a' && ch <= 'z') return (int)(ch - 'a' + 'A');
		if (ch >= '0' && ch <= '9') return (int)ch;
		if (ch == ' ') return VK_SPACE;
		if (ch == '\t') return VK_TAB;
		if (ch == '\r') return VK_RETURN;
		return (int)(unsigned char)ch;
	}

	private: char KeyCodeToChar(System::Windows::Forms::Keys keyCode) {
		if (keyCode >= System::Windows::Forms::Keys::A && keyCode <= System::Windows::Forms::Keys::Z) return (char)keyCode;
		if (keyCode >= System::Windows::Forms::Keys::D0 && keyCode <= System::Windows::Forms::Keys::D9) return (char)('0' + ((int)keyCode - (int)System::Windows::Forms::Keys::D0));
		if (keyCode >= System::Windows::Forms::Keys::NumPad0 && keyCode <= System::Windows::Forms::Keys::NumPad9) return (char)('0' + ((int)keyCode - (int)System::Windows::Forms::Keys::NumPad0));
		return ' ';
	}

		   // Native Windows Win32 API event processing sequence logic
	private: void SendClickNative(int vk) {
		UINT scanCode = ::MapVirtualKey((UINT)vk, MAPVK_VK_TO_VSC);

		INPUT inputs[2] = {};

		// KEY DOWN Setup
		inputs[0].type = INPUT_KEYBOARD;
		inputs[0].ki.wVk = (WORD)vk;
		inputs[0].ki.wScan = (WORD)scanCode;
		inputs[0].ki.dwFlags = (scanCode ? KEYEVENTF_SCANCODE : 0);

		// KEY UP Setup
		inputs[1].type = INPUT_KEYBOARD;
		inputs[1].ki.wVk = (WORD)vk;
		inputs[1].ki.wScan = (WORD)scanCode;
		inputs[1].ki.dwFlags = KEYEVENTF_KEYUP | (scanCode ? KEYEVENTF_SCANCODE : 0);

		::SendInput(2, inputs, sizeof(INPUT));
	}

	private: void ClickLoop() {
		while (true) {
			System::Threading::Monitor::Enter(m_lock);
			bool shouldRun;
			try {
				shouldRun = m_running;
				if (!shouldRun) break;
				if (!m_active) {
					shouldRun = false;
				}
			}
			finally {
				System::Threading::Monitor::Exit(m_lock);
			}

			if (!shouldRun) {
				System::Threading::Thread::Sleep(5);
				continue;
			}

			int cps;
			long long last;
			System::Threading::Monitor::Enter(m_lock);
			try {
				cps = m_cps;
				last = m_lastQpc;
			}
			finally {
				System::Threading::Monitor::Exit(m_lock);
			}

			if (cps < 1) cps = 1;
			if (cps > 999) cps = 999;

			LARGE_INTEGER now;
			QueryPerformanceCounter(&now);
			long long ticksPerClick = m_qpcFreq / cps;

			// FIX: Prevent burst backlogging if thread wakes up behind schedule
			if (now.QuadPart - last > (ticksPerClick * 2)) {
				last = now.QuadPart - ticksPerClick;
			}

			while (now.QuadPart - last >= ticksPerClick) {
				SendClickNative(m_spamKeyVk);
				System::Threading::Monitor::Enter(m_lock);
				try {
					m_sampleClicks++;
					m_totalClicks++;
				}
				finally {
					System::Threading::Monitor::Exit(m_lock);
				}
				last += ticksPerClick;
			}
			System::Threading::Monitor::Enter(m_lock);
			try {
				m_lastQpc = last;
			}
			finally {
				System::Threading::Monitor::Exit(m_lock);
			}
			System::Threading::Thread::Sleep(1);
		}
	}

	private: void ToggleMacro() {
		System::Threading::Monitor::Enter(m_lock);
		bool nowActive;
		try {
			nowActive = !m_active;
			m_active = nowActive;

			// FIX: Clear sample counts immediately upon change
			m_sampleClicks = 0;

			if (nowActive) {
				// FIX: Snap timestamp anchor forward to current time to stop catch-up bursts
				LARGE_INTEGER t;
				QueryPerformanceCounter(&t);
				m_lastQpc = t.QuadPart;
			}
		}
		finally {
			System::Threading::Monitor::Exit(m_lock);
		}

		System::String^ bindStr = keybind_txtbox->Text->ToUpper();

		if (nowActive) {
			SendClickNative(m_spamKeyVk);
			System::Threading::Monitor::Enter(m_lock);
			try {
				m_totalClicks++;
				m_sampleClicks++;
			}
			finally {
				System::Threading::Monitor::Exit(m_lock);
			}
			this->statusLabel->Text = L"\u25CF LIVE";
			this->statusLabel->ForeColor = System::Drawing::Color::LimeGreen;
			this->toggleButton->Text = L"\u25A0  STOP    [" + bindStr + L"]";
		}
		else {
			this->statusLabel->Text = L"\u25CF IDLE";
			this->statusLabel->ForeColor = System::Drawing::Color::OrangeRed;
			this->toggleButton->Text = L"\u25B6  START   [" + bindStr + L"]";
		}
	}
	private: System::Void toggleButton_Click(System::Object^ sender, System::EventArgs^ e) {
		ToggleMacro();
	}

	private: System::Void statsTimer_Tick(System::Object^ sender, System::EventArgs^ e) {
		System::Threading::Monitor::Enter(m_lock);
		try {
			if (m_active) {
				int sample = m_sampleClicks;
				m_sampleClicks = 0;
				int rate = sample * 4;
				this->liveCpsLabel->Text = System::String::Format("Live CPS: {0}", rate);
			}
			else {
				m_sampleClicks = 0;
				this->liveCpsLabel->Text = L"Live CPS: 0";
			}
			long long total = m_totalClicks;
			this->totalClicksLabel->Text = System::String::Format("Total Clicks: {0}", total);
		}
		finally {
			System::Threading::Monitor::Exit(m_lock);
		}
	}

	private: System::Void MainForm_Load(System::Object^ sender, System::EventArgs^ e) {
		LARGE_INTEGER freq;
		QueryPerformanceFrequency(&freq);
		m_qpcFreq = freq.QuadPart;
		LARGE_INTEGER now;
		QueryPerformanceCounter(&now);
		System::Threading::Monitor::Enter(m_lock);
		try {
			m_lastQpc = now.QuadPart;
		}
		finally {
			System::Threading::Monitor::Exit(m_lock);
		}

		timeBeginPeriod(1);

		if (this->textBox1->Text->Length > 0) {
			char ch = this->textBox1->Text[0];
			System::Threading::Monitor::Enter(m_lock);
			try {
				m_spamKeyVk = CharToVkCode(ch);
			}
			finally {
				System::Threading::Monitor::Exit(m_lock);
			}
		}

		HWND hwnd = (HWND)(this->Handle.ToPointer());
		RegisterHotKey(hwnd, TOGGLE_HOTKEY_ID, MOD_NOREPEAT, m_toggleKeyVk);

		UpdateCpsFromComboBox();
		m_clickThread = gcnew System::Threading::Thread(gcnew System::Threading::ThreadStart(this, &MainForm::ClickLoop));
		m_clickThread->IsBackground = true;
		m_clickThread->Priority = System::Threading::ThreadPriority::Highest;
		m_clickThread->Start();

		this->statsTimer->Start();
	}

	private: System::Void MainForm_FormClosing(System::Object^ sender, System::Windows::Forms::FormClosingEventArgs^ e) {
		HWND hwnd = (HWND)(this->Handle.ToPointer());
		UnregisterHotKey(hwnd, TOGGLE_HOTKEY_ID);
		System::Threading::Monitor::Enter(m_lock);
		try {
			m_running = false;
		}
		finally {
			System::Threading::Monitor::Exit(m_lock);
		}
		if (m_clickThread != nullptr) {
			m_clickThread->Join();
		}
		timeEndPeriod(1);
	}
	};
}